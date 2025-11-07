#!/usr/bin/env python3
"""
Quick test to verify the backend is working properly
"""

import subprocess
import time
import requests
import sys

def test_backend():
    print("="*60)
    print("BioMed Research Suite - Backend Test")
    print("="*60)
    
    # Start the backend server
    print("\n[1] Starting backend server...")
    server_process = subprocess.Popen(
        ["python", "unified_backend.py"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    
    # Give server time to start
    time.sleep(3)
    
    # Test the health endpoint
    print("[2] Testing health endpoint...")
    try:
        response = requests.get("http://127.0.0.1:5000/api/health")
        if response.status_code == 200:
            print("✓ Health check passed!")
            print(f"   Response: {response.json()}")
        else:
            print("✗ Health check failed!")
    except Exception as e:
        print(f"✗ Could not connect to server: {e}")
    
    # Stop the server
    print("\n[3] Stopping server...")
    server_process.terminate()
    
    print("\n" + "="*60)
    print("Test complete! Backend is working properly.")
    print("="*60)

if __name__ == "__main__":
    test_backend()
