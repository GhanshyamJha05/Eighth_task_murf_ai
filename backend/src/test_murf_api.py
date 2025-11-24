"""
Test script to verify Murf API connection and voice synthesis.
"""
import os
import requests
from dotenv import load_dotenv

load_dotenv(".env.local")

def test_murf_api():
    api_key = os.environ.get("MURF_API_KEY")
    
    if not api_key:
        print("❌ MURF_API_KEY not found in environment")
        return False
    
    print(f"✓ API Key found: {api_key[:10]}...")
    
    # Test with different possible endpoints
    endpoints = [
        "https://api.murf.ai/v1/speech/generate",
        "https://api.murf.ai/v1/speech/synthesize",
        "https://api.murf.ai/v2/speech/generate"
    ]
    
    voices = ['en-US-ryan', 'en-US-alicia', 'en-US-ken']
    
    for endpoint in endpoints:
        print(f"\n🔍 Testing endpoint: {endpoint}")
        
        for voice in voices:
            payload = {
                "text": "Hello, this is a test.",
                "voiceId": voice,
                "style": "Conversation",
                "format": "WAV",
                "sampleRate": 24000,
                "channelType": "MONO"
            }
            
            headers = {
                "api-key": api_key,
                "Content-Type": "application/json"
            }
            
            try:
                print(f"  Testing voice: {voice}...", end=" ")
                response = requests.post(endpoint, json=payload, headers=headers, timeout=10)
                
                if response.status_code == 200:
                    print(f"✓ SUCCESS (status: {response.status_code})")
                    print(f"    Response keys: {list(response.json().keys())}")
                    return True
                else:
                    print(f"✗ Failed (status: {response.status_code})")
                    print(f"    Response: {response.text[:200]}")
                    
            except Exception as e:
                print(f"✗ Error: {e}")
    
    print("\n❌ All endpoints failed. Please check:")
    print("  1. Your MURF_API_KEY is valid")
    print("  2. You have access to Murf Falcon API")
    print("  3. The voice IDs are correct")
    return False

if __name__ == "__main__":
    print("=" * 60)
    print("Murf API Connection Test")
    print("=" * 60)
    test_murf_api()
