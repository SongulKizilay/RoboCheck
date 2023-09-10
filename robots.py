import subprocess
import sys

def main():
    # subdomaintxt.txt dosyasını oku
    with open('/root/Desktop/subdomain.txt', 'r') as subdomain_file:
        subdomains = subdomain_file.read().splitlines()

    try:
        # Subdomainleri döngü ile işle
        for subdomain in subdomains:
            # ctrl+c yapılınca programı sonlandırmak için KeyboardInterrupt'i yakala
            try:
                subdomain_url = subdomain.strip()  # Boşlukları kaldırın
                result = subprocess.check_output(['curl', '-sk', subdomain_url], stderr=subprocess.STDOUT)
                result = result.decode('utf-8')
                print(f"Subdomain: {subdomain_url}\n")
                print(result)
                print('-' * 50)
            except subprocess.CalledProcessError as e:
                if "Hata: Command" in e.output.decode('utf-8'):
                    print(f"Host bulunamıyor: {subdomain_url}\n")
                else:
                    print(f"Hata: {e}")
    except KeyboardInterrupt:
        print("Kod kullanıcı tarafından sonlandırıldı.")
        sys.exit(0)

if __name__ == "__main__":
    main()
