from google import genai
from google.genai.errors import APIError
from typing import List
from ..database import settings

class KeyPointExtractor:
    def __init__(self):
        self.api_key = settings.GEMINI_API_KEY
        if self.api_key == "dummy_key":
             print("WARNING: GEMINI_API_KEY is not set correctly. Keypoint extraction will fail.")
        self.client = genai.Client(api_key=self.api_key)
        self.model = 'gemini-2.5-flash'

    def extract(self, review_text: str) -> List[str]:
        """Menggunakan Gemini untuk mengekstrak poin-poin utama dari ulasan."""
        if self.api_key == "dummy_key":
            return ["API Key Error: Gemini key not configured."]
            
        prompt = f"""
        Ekstraksi dan buat poin-poin utama (minimal 3, maksimal 5) dari ulasan produk berikut. 
        Sajikan output sebagai daftar yang dipisahkan oleh baris baru dan diawali tanda pisah ('-').
        Contoh format output:
        - Poin Utama 1
        - Poin Utama 2

        Ulasan: "{review_text}"
        """

        try:
            response = self.client.models.generate_content(
                model=self.model,
                contents=prompt,
                config={"temperature": 0.2} 
            )
            
            key_points_text = response.text.strip()
            
            key_points = [
                point.strip('- ').strip() 
                for point in key_points_text.split('\n') 
                if point.strip()
            ]
            
            return key_points
        except APIError as e:
            print(f"Gemini API Error: {e}")
            return [f"API Error: Failed to communicate with Gemini. ({e})"]
        except Exception as e:
            print(f"An unexpected error occurred during extraction: {e}")
            return [f"Extraction Error: {str(e)}"]