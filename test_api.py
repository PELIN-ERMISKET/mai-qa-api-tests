import pytest
import requests
import json
from datetime import datetime


class TestUserManagementAPI:
    """
    Postman collection'ına dayalı Kullanıcı Yönetimi API'si için test paketi
    """
    
    @pytest.fixture(scope="class")
    def base_url(self):
        """API için temel URL"""
        return "http://localhost:8000"  # Gerçek base URL ile güncelleyin
    
    @pytest.fixture(scope="class")
    def admin_credentials(self):
        """Kimlik doğrulama için admin bilgileri"""
        return {
            "username": "admin_user",
            "password": "Admin@2024"
        }
    
    @pytest.fixture(scope="class")
    def auth_token(self, base_url, admin_credentials):
        """Kimlik doğrulama token'ı al"""
        response = requests.post(f"{base_url}/login", json=admin_credentials)
        if response.status_code == 200:
            # Collection'dan görüldüğü üzere login endpoint sadece başarı döndürüyor
            # Token almak için başka bir endpoint gerekebilir
            # Bu durumda mock token kullanacağız
            return "mock_token_for_testing"
        return None
    
    @pytest.fixture
    def valid_user_data(self):
        """Test için geçerli kullanıcı verisi"""
        timestamp = int(datetime.now().timestamp())
        return {
            "username": f"test_user_{timestamp}",
            "email": f"test_{timestamp}@example.com",
            "password": "TestPass123",
            "age": 25,
            "phone": f"+1555{timestamp % 10000000:07d}"
        }
    
    @pytest.fixture
    def headers(self, auth_token):
        """Kimlik doğrulaması ile header'lar"""
        headers = {"Content-Type": "application/json"}
        if auth_token:
            headers["Authorization"] = f"Bearer {auth_token}"
        return headers
    
    @pytest.fixture
    def basic_auth_headers(self, admin_credentials):
        """Admin işlemleri için Basic auth header'ları"""
        import base64
        credentials = f"{admin_credentials['username']}:{admin_credentials['password']}"
        encoded_credentials = base64.b64encode(credentials.encode()).decode()
        return {
            "Authorization": f"Basic {encoded_credentials}",
            "Content-Type": "application/json"
        }


class TestUserCreation(TestUserManagementAPI):
    """Kullanıcı oluşturma fonksiyonlarını test et"""
    
    def test_create_user_success(self, base_url, valid_user_data):
        """Başarılı kullanıcı oluşturma testi"""
        response = requests.post(f"{base_url}/users", json=valid_user_data)
        
        assert response.status_code == 201
        data = response.json()
        assert data["username"] == valid_user_data["username"]
        assert data["email"] == valid_user_data["email"]
        assert data["age"] == valid_user_data["age"]
        assert "password" not in data  # Şifre döndürülmemeli
        assert "id" in data
        assert "created_at" in data
        assert data["is_active"] is True
    
    def test_create_user_duplicate_username(self, base_url):
        """Tekrarlanan kullanıcı adıyla kullanıcı oluşturma testi"""
        user_data = {
            "username": "john_doe",  # Bu kullanıcının var olduğunu varsayıyoruz
            "email": "duplicate@example.com",
            "password": "password123",
            "age": 30,
            "phone": "+15551234567"
        }
        
        response = requests.post(f"{base_url}/users", json=user_data)
        # Tekrarlanan kullanıcı adı için 422 veya 400 dönmeli
        assert response.status_code in [400, 422]
    
    def test_create_user_invalid_email(self, base_url):
        """Geçersiz email ile kullanıcı oluşturma testi"""
        user_data = {
            "username": "test_invalid_email",
            "email": "@example.com",  # Geçersiz email
            "password": "password123",
            "age": 25,
            "phone": "+15551234567"
        }
        
        response = requests.post(f"{base_url}/users", json=user_data)
        assert response.status_code == 422
    
    def test_create_user_username_too_short(self, base_url):
        """Çok kısa kullanıcı adı ile kullanıcı oluşturma testi"""
        user_data = {
            "username": "ab",  # Çok kısa
            "email": "short@example.com",
            "password": "password123",
            "age": 25,
            "phone": "+15551234567"
        }
        
        response = requests.post(f"{base_url}/users", json=user_data)
        assert response.status_code == 422
    
    def test_create_user_username_too_long(self, base_url):
        """Çok uzun kullanıcı adı ile kullanıcı oluşturma testi"""
        user_data = {
            "username": "a" * 51,  # Çok uzun (51 karakter)
            "email": "long@example.com",
            "password": "password123",
            "age": 25,
            "phone": "+15551234567"
        }
        
        response = requests.post(f"{base_url}/users", json=user_data)
        assert response.status_code == 422
    
    def test_create_user_age_boundaries(self, base_url):
        """Yaş sınır değerleri ile kullanıcı oluşturma testi"""
        timestamp = int(datetime.now().timestamp())
        
        # Minimum yaş testi
        user_data_min = {
            "username": f"min_age_user_{timestamp}",
            "email": f"min_{timestamp}@example.com",
            "password": "password123",
            "age": 18,
            "phone": f"+1555{timestamp % 10000000:07d}"
        }
        
        response = requests.post(f"{base_url}/users", json=user_data_min)
        assert response.status_code == 201
        
        # Maksimum yaş testi
        user_data_max = {
            "username": f"max_age_user_{timestamp}",
            "email": f"max_{timestamp}@example.com",
            "password": "password123",
            "age": 150,
            "phone": f"+1555{timestamp % 10000000 + 1:07d}"
        }
        
        response = requests.post(f"{base_url}/users", json=user_data_max)
        assert response.status_code == 201
    
    def test_create_user_invalid_age(self, base_url):
        """Geçersiz yaş ile kullanıcı oluşturma testi"""
        timestamp = int(datetime.now().timestamp())
        
        # Çok düşük yaş
        user_data = {
            "username": f"invalid_age_{timestamp}",
            "email": f"invalid_{timestamp}@example.com",
            "password": "password123",
            "age": 17,
            "phone": f"+1555{timestamp % 10000000:07d}"
        }
        
        response = requests.post(f"{base_url}/users", json=user_data)
        assert response.status_code == 422
        
        # Çok yüksek yaş
        user_data["age"] = 151
        user_data["username"] = f"invalid_age_high_{timestamp}"
        
        response = requests.post(f"{base_url}/users", json=user_data)
        assert response.status_code == 422
    
    def test_create_user_invalid_phone(self, base_url):
        """Geçersiz telefon numarası ile kullanıcı oluşturma testi"""
        timestamp = int(datetime.now().timestamp())
        
        user_data = {
            "username": f"invalid_phone_{timestamp}",
            "email": f"phone_{timestamp}@example.com",
            "password": "password123",
            "age": 25,
            "phone": "invalid-phone"
        }
        
        response = requests.post(f"{base_url}/users", json=user_data)
        assert response.status_code == 422
    
    def test_create_user_missing_required_fields(self, base_url):
        """Zorunlu alanları eksik kullanıcı oluşturma testi"""
        # Kullanıcı adı eksik
        user_data = {
            "email": "missing@example.com",
            "password": "password123",
            "age": 25
        }
        
        response = requests.post(f"{base_url}/users", json=user_data)
        assert response.status_code == 422


class TestUserRetrieval(TestUserManagementAPI):
    """Kullanıcı sorgulama fonksiyonlarını test et"""
    
    def test_get_user_success(self, base_url):
        """Başarılı kullanıcı sorgulama testi"""
        user_id = 1  # ID 1 olan kullanıcının var olduğunu varsayıyoruz
        response = requests.get(f"{base_url}/users/{user_id}")
        
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == user_id
        assert "username" in data
        assert "email" in data
        assert "password" not in data  # Şifre döndürülmemeli
    
    def test_get_user_not_found(self, base_url):
        """Var olmayan kullanıcı sorgulama testi"""
        user_id = 99999  # Bu kullanıcının var olmadığını varsayıyoruz
        response = requests.get(f"{base_url}/users/{user_id}")
        
        assert response.status_code == 404
    
    def test_list_users(self, base_url):
        """Kullanıcıları listeleme testi"""
        response = requests.get(f"{base_url}/users")
        
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        
        if len(data) > 0:
            user = data[0]
            assert "id" in user
            assert "username" in user
            assert "password" not in user
    
    def test_list_users_with_pagination(self, base_url):
        """Sayfalama ile kullanıcıları listeleme testi"""
        response = requests.get(f"{base_url}/users", params={
            "limit": 5,
            "offset": 0,
            "sort_by": "id",
            "order": "asc"
        })
        
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) <= 5
    
    def test_search_users(self, base_url):
        """Kullanıcı arama fonksiyonu testi"""
        response = requests.get(f"{base_url}/users/search", params={
            "q": "john",
            "field": "all",
            "exact": "false"
        })
        
        assert response.status_code == 200


class TestUserUpdate(TestUserManagementAPI):
    """Kullanıcı güncelleme fonksiyonlarını test et"""
    
    def test_update_user_with_bearer_token(self, base_url, headers):
        """Bearer token ile kullanıcı güncelleme testi"""
        if not headers.get("Authorization"):
            pytest.skip("Kimlik doğrulama token'ı mevcut değil")
            
        user_id = 7  # Kullanıcının var olduğunu varsayıyoruz
        update_data = {
            "email": "updated_email@example.com",
            "age": 30,
            "phone": "+19175551235"
        }
        
        response = requests.put(f"{base_url}/users/{user_id}", 
                              json=update_data, headers=headers)
        
        # Doğru kimlik doğrulama ile başarılı olmalı
        assert response.status_code == 200
    
    def test_update_user_without_auth(self, base_url):
        """Kimlik doğrulama olmadan kullanıcı güncelleme testi"""
        user_id = 7
        update_data = {
            "email": "unauthorized@example.com"
        }
        
        response = requests.put(f"{base_url}/users/{user_id}", json=update_data)
        
        # Kimlik doğrulama olmadan başarısız olmalı
        assert response.status_code in [401, 403]
    
    def test_update_user_invalid_phone(self, base_url, headers):
        """Geçersiz telefon numarası ile kullanıcı güncelleme testi"""
        if not headers.get("Authorization"):
            pytest.skip("Kimlik doğrulama token'ı mevcut değil")
            
        user_id = 7
        update_data = {
            "phone": "+1917555123456789"  # Çok uzun
        }
        
        response = requests.put(f"{base_url}/users/{user_id}", 
                              json=update_data, headers=headers)
        
        assert response.status_code == 422
    
    def test_update_user_with_username_should_fail(self, base_url, headers):
        """Kullanıcı adı güncellemenin başarısız olması testi (BUG-008 temel alınarak)"""
        if not headers.get("Authorization"):
            pytest.skip("Kimlik doğrulama token'ı mevcut değil")
            
        user_id = 11
        update_data = {
            "username": "hacker_takeover",
            "phone": "+19175551234"
        }
        
        response = requests.put(f"{base_url}/users/{user_id}", 
                              json=update_data, headers=headers)
        
        # Kullanıcı adı güncellemeleri kısıtlanmalı
        # Bu başarılı olursa potansiyel güvenlik açığı
        if response.status_code == 200:
            pytest.fail("Kullanıcı adı güncelleme başarılı - potansiyel güvenlik sorunu")


class TestUserDeletion(TestUserManagementAPI):
    """Kullanıcı silme fonksiyonlarını test et"""
    
    def test_delete_user_with_basic_auth(self, base_url, basic_auth_headers):
        """Basic authentication ile kullanıcı silme testi"""
        # Önce silinecek kullanıcıyı oluştur
        user_data = {
            "username": f"delete_test_{int(datetime.now().timestamp())}",
            "email": f"delete_{int(datetime.now().timestamp())}@example.com",
            "password": "password123",
            "age": 25
        }
        
        create_response = requests.post(f"{base_url}/users", json=user_data)
        if create_response.status_code == 201:
            user_id = create_response.json()["id"]
            
            # Şimdi kullanıcıyı sil
            response = requests.delete(f"{base_url}/users/{user_id}", 
                                     headers=basic_auth_headers)
            
            assert response.status_code == 200
    
    def test_delete_user_without_auth(self, base_url):
        """Kimlik doğrulama olmadan kullanıcı silme testi"""
        user_id = 39
        response = requests.delete(f"{base_url}/users/{user_id}")
        
        assert response.status_code in [401, 403]
    
    def test_delete_user_with_wrong_auth_scheme(self, base_url, headers):
        """Yanlış kimlik doğrulama şeması ile kullanıcı silme testi"""
        user_id = 39
        response = requests.delete(f"{base_url}/users/{user_id}", headers=headers)
        
        # DELETE işlemi basic auth gerektirdiği için bearer ile başarısız olmalı
        assert response.status_code in [401, 403]
    
    def test_delete_non_existent_user(self, base_url, basic_auth_headers):
        """Var olmayan kullanıcıyı silme testi"""
        user_id = 26585  # Var olmayan kullanıcı
        response = requests.delete(f"{base_url}/users/{user_id}", 
                                 headers=basic_auth_headers)
        
        # Nazikçe handle edilmeli (404 veya 200 dönebilir)
        assert response.status_code in [200, 404]
    
    def test_delete_idempotent(self, base_url, basic_auth_headers):
        """Silme işleminin idempotent olması testi"""
        user_id = 11
        
        # İki kez sil
        response1 = requests.delete(f"{base_url}/users/{user_id}", 
                                  headers=basic_auth_headers)
        response2 = requests.delete(f"{base_url}/users/{user_id}", 
                                  headers=basic_auth_headers)
        
        # Her ikisi de başarılı olmalı (idempotent)
        assert response1.status_code == 200
        assert response2.status_code == 200


class TestAuthentication(TestUserManagementAPI):
    """Kimlik doğrulama fonksiyonlarını test et"""
    
    def test_login_success(self, base_url, admin_credentials):
        """Başarılı giriş testi"""
        response = requests.post(f"{base_url}/login", json=admin_credentials)
        
        assert response.status_code == 200
        # Login endpoint might return token or just success message
        data = response.json()
        # Check if response contains token or is just a success response
    
    def test_login_wrong_password(self, base_url):
        """Yanlış şifre ile giriş testi"""
        credentials = {
            "username": "admin_user",
            "password": "YanlisPassword"
        }
        
        response = requests.post(f"{base_url}/login", json=credentials)
        assert response.status_code in [401, 403]
    
    def test_login_non_existent_user(self, base_url):
        """Var olmayan kullanıcı ile giriş testi"""
        credentials = {
            "username": "var_olmayan_kullanici",
            "password": "password123"
        }
        
        response = requests.post(f"{base_url}/login", json=credentials)
        assert response.status_code in [401, 403, 404]
    
    def test_login_missing_password(self, base_url):
        """Eksik şifre ile giriş testi"""
        credentials = {
            "username": "admin_user"
        }
        
        response = requests.post(f"{base_url}/login", json=credentials)
        assert response.status_code == 422
    
    def test_logout(self, base_url, headers):
        """Çıkış testi"""
        if not headers.get("Authorization"):
            pytest.skip("Kimlik doğrulama token'ı mevcut değil")
            
        response = requests.post(f"{base_url}/logout", headers=headers)
        assert response.status_code == 200
    
    def test_logout_invalid_token(self, base_url):
        """Geçersiz token ile çıkış testi"""
        headers = {
            "Authorization": "Bearer gecersiz_token"
        }
        
        response = requests.post(f"{base_url}/logout", headers=headers)
        # Implementasyona göre 401 veya 200 dönebilir
        assert response.status_code in [200, 401]


class TestSystemEndpoints(TestUserManagementAPI):
    """Sistem endpoint'lerini test et"""
    
    def test_health_check(self, base_url):
        """Sistem sağlık kontrolü testi"""
        response = requests.get(f"{base_url}/health")
        
        assert response.status_code == 200
        data = response.json()
        assert "status" in data or "memory_sessions" in data
    
    def test_stats_endpoint(self, base_url):
        """İstatistik endpoint testi"""
        response = requests.get(f"{base_url}/stats", params={"include_details": False})
        
        assert response.status_code == 200
    
    def test_stats_with_details(self, base_url):
        """Detaylı istatistik endpoint testi (potansiyel güvenlik sorunu - BUG-011)"""
        response = requests.get(f"{base_url}/stats", params={"include_details": True})
        
        # Bu hassas bilgileri açığa çıkarabilir
        if response.status_code == 200:
            data = response.json()
            # Hassas veri açığa çıkıp çıkmadığını kontrol et
            sensitive_keys = ["password", "secret", "key", "token"]
            response_text = str(data).lower()
            
            for key in sensitive_keys:
                if key in response_text:
                    pytest.fail(f"Potansiyel güvenlik sorunu: {key} stats endpoint'inde açığa çıktı")
    
    def test_root_endpoint(self, base_url):
        """Ana endpoint testi"""
        response = requests.get(f"{base_url}/")
        
        assert response.status_code == 200


class TestSecurityVulnerabilities(TestUserManagementAPI):
    """Bilinen güvenlik açıklarını test et"""
    
    def test_sql_injection_in_user_id(self, base_url, basic_auth_headers):
        """Kullanıcı ID parametresinde SQL injection testi"""
        malicious_id = "1 OR 1=1"
        response = requests.delete(f"{base_url}/users/{malicious_id}", 
                                 headers=basic_auth_headers)
        
        # Kötü niyetli girdiyi nazikçe handle etmeli
        assert response.status_code in [400, 422, 404]
    
    def test_unauthorized_user_deletion(self, base_url):
        """Yetkisiz kullanıcı silme testi (BUG-009, BUG-010)"""
        # Uygun yetki olmadan kullanıcı silmeye çalış
        user_ids = [4, 41]
        
        for user_id in user_ids:
            # Farklı bir kullanıcının kimlik bilgilerini kullan
            fake_credentials = {
                "username": "attacker_1758004274",
                "password": "oldnew1"
            }
            
            import base64
            credentials = f"{fake_credentials['username']}:{fake_credentials['password']}"
            encoded = base64.b64encode(credentials.encode()).decode()
            
            headers = {"Authorization": f"Basic {encoded}"}
            
            response = requests.delete(f"{base_url}/users/{user_id}", headers=headers)
            
            # Yetkisiz silmeye izin vermemeli
            if response.status_code == 200:
                pytest.fail(f"Güvenlik açığı: Yetkisiz kullanıcı {user_id} silme işlemi başarılı")
    
    def test_phone_number_with_leading_zeros(self, base_url):
        """Başında sıfır olan telefon numarası validasyon testi (BUG-004)"""
        timestamp = int(datetime.now().timestamp())
        user_data = {
            "username": f"phone_test_{timestamp}",
            "email": f"phone_{timestamp}@example.com",
            "password": "password123",
            "age": 25,
            "phone": "+0049265680"  # Ülke kodundan sonra başında sıfır
        }
        
        response = requests.post(f"{base_url}/users", json=user_data)
        
        # Telefon numarası formatını düzgün validate etmeli
        if response.status_code == 201:
            pytest.fail("Geçersiz formattaki telefon numarası kabul edildi")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])