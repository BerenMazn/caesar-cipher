def caesar_cipher(text, shift, mode='encrypt'):
    result = ""

    if mode == 'decrypt':
        shift = -shift
        
    for char in text:
        if char.isalpha():
    
            ascii_offset = ord('A') if char.isupper() else ord('a')
           
            shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            result += shifted_char
        else:
            
            result += char
            
    return result

def main():
    print("=== CAESAR CIPHER (SEZAR ŞİFRELEMESİ) ===")
    print("1. Metni Şifrele")
    print("2. Şifreyi Çöz")
    
    choice = input("Seçiminiz (1 veya 2): ").strip()
    
    if choice == '1':
        text = input("Şifrelenecek metni girin: ")
        shift = int(input("Kaydırma miktarını (anahtar) girin (örn: 3): "))
        encrypted = caesar_cipher(text, shift, 'encrypt')
        print(f"\n[+] Şifrelenmiş Metin: {encrypted}")
    elif choice == '2':
        text = input("Çözülecek şifreli metni girin: ")
        shift = int(input("Kaydırma miktarını (anahtar) girin (örn: 3): "))
        decrypted = caesar_cipher(text, shift, 'decrypt')
        print(f"\n[+] Çözülmüş Metin: {decrypted}")
    else:
        print("[-] Geçersiz seçim!")

if __name__ == "__main__":
    main()