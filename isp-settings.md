---
layout: page
title: ISP Settings
---
### Standard Fibre Settings {#standard_settings}

- Operating Mode: Fibre or Ethernet WAN
- Connection Type: Dynamic IP, IPoE (IP over Ethernet), Automatic IP or DHCP
- MTU or MRU: 1492 or 1500
- VLAN or 802.1q: Enabled
- VLAN ID: 10
- VLAN Priority or 802.1p: 0

### ISP Specific
#### List
- [2Degrees](#two_degrees)
- [Bigpipe](#bigpipe)
- [Contact Energy](#contact_energy)
- [Hotshot](#hotshot)
- [Mercury](#mercury)
- [One NZ](#one_nz)
- [Skinny](#skinny)
- [Spark](#spark)
- [Trustpower](#trustpower)

<!-- TEMPLATE
---

#### Provider_Name
##### ADSL

- Operating Mode: ADSL or ATM
- PPP Protocol: 
- PPP Username: 
- PPP Password: 
- PPP Mode: 
- VPI: 
- VCI: 
- Multiplexing: 
- VLAN or 802.1q: 
- VLAN ID: 
- VLAN Priority or 802.1p: 
- MTU: 
- Authentication mode: 
- NAT: 
- IP Protocal Version: 
- IPv4 Address Type: 
- IPv6 Address Type: 
- Primary (Preferred) DNS: 
- Secondary DNS: 

##### VDSL

- Operating Mode: VDSL or PTM
- PPP Protocol: 
- PPP Username: 
- PPP Password: 
- PPP Mode: 
- PCP: 
- VPI: 
- VCI: 
- VLAN or 802.1q: 
- VLAN ID: 
- VLAN Priority or 802.1p: 
- MTU: 
- Authentication mode: 
- NAT: 
- IP Protocal Version: 
- IPv4 Address Type: 
- IPv6 Address Type: 
- Primary (Preferred) DNS: 
- Secondary DNS: 

##### FIBRE

- Operating Mode: Fibre or Ethernet WAN
- Access Type: 
- VPI: 
- VCI: 
- VLAN or 802.1q: 
- VLAN ID: 
- VLAN Priority or 802.1p: 
- MTU: 
- Authentication mode: 
- NAT: 
- IP Protocal Version: 
- IPv4 Address Type: 
- IPv6 Address Type: 
- Primary (Preferred) DNS: 
- Secondary DNS: 

##### VoIP
-->

#### 2Degrees {#two_degrees}
##### ADSL

- Operating Mode: ADSL or ATM
- PPP Protocol: PPP over ATM (PPPoA)
- PPP Username: putanything@2degrees.nz
- PPP Password: putanything
- PPP Mode: VCMUX
- VPI: 0
- VCI: 100
- VLAN Priority or 802.1p: 
- MTU: 1492 or 1500

##### VDSL

- Operating Mode: VDSL or PTM
- PPP Protocol: PPP over Ethernet (PPPoE)
- PPP Username: putanything@2degrees.nz
- PPP Password: putanything
- PCP: 0
- VLAN or 802.1q: Enabled
- VLAN ID: 10
- VLAN Priority or 802.1p: 0
- MTU: 1492 or 1500
- Authentication Mode: PAP
- NAT: Enabled

##### FIBRE

[Standard Settings](#standard_settings)

##### VoIP

For ADSL/VDSL: Not disclosed
For Fibre: This is provided via the Optical Network Terminal, no configuration needed

---

#### Bigpipe {#bigpipe}
##### ADSL

- Operating Mode: ADSL or ATM
- PPP Protocol: PPP over ATM (PPPoA)
- PPP Username: Bigpipe
- PPP Password: Bigpipe
- VPI: 0
- VCI: 100
- Multiplexing: VCMUX
- MTU: 1492

##### VDSL

- Operating Mode: VDSL or PTM
- PPP Protocol: PPP over Ethernet (PPPoE)
- PPP Username: Anything
- PPP Password: Anything
- VLAN or 802.1q: Enabled
- VLAN ID: 10
- VLAN Priority or 802.1p: 0
- MTU: 1492

##### FIBRE

- Operating Mode: Fibre or Ethernet WAN
- PPP Protocol: PPP over Ethernet (PPPoE)
- PPP Username: Anything
- PPP Password: Anything
- MTU: 1492

##### VoIP

Not disclosed

---

#### Contact Energy {#contact_energy}
##### ADSL

- Operating Mode: ADSL or ATM
- PPP Protocol: PPPoE
- PPP Username: user@contactenergy.co.nz
- PPP Password: c0nt4ct-3n3rgy!
- PPP Mode: Always On
- VPI: 0
- VCI: 110
- VLAN or 802.1q: Enabled
- VLAN ID: 10
- VLAN Priority or 802.1p: 0
- MTU: 1492 or 1500
- Authentication mode: PAP
- NAT: Enabled, Full Cone

##### VDSL

- Operating Mode: VDSL or PTM
- PPP Protocol: PPPoE
- PPP Username: user@contactenergy.co.nz
- PPP Password: c0nt4ct-3n3rgy!
- PPP Mode: Always On
- VPI: 0
- VCI: 110
- VLAN or 802.1q: Enabled
- VLAN ID: 10
- VLAN Priority or 802.1p: 0
- MTU: 1492 or 1500
- Authentication mode: PAP
- NAT: Enabled, Full Cone

##### FIBRE

[Standard Settings](#standard_settings)

##### VoIP

Not disclosed

---

#### Hotshot {#hotshot}
##### ADSL

Doesn't service

##### VDSL

Doesn't service

##### FIBRE

- Operating Mode: Fibre or Ethernet WAN
- PPP Protocol: PPP over Ethernet (PPPoE)
- PPP Username: HotShotFibre
- PPP Password: UrDaBest
- VLAN or 802.1q:
    - If you joined before 01/06/2020 and are:
        - In Auckland: Disabled
        - Outside of Auckland: Enabled
    - If you joined on/after 01/06/2020: Disabled
- VLAN ID:
    - If you joined before 01/06/2020 and are outside of Auckland: 10
- VLAN Priority or 802.1p:
    - If you joined before 01/06/2020 and are outside of Auckland: 0
- MTU: 1492
- MSS: 1452

##### VoIP

Doesn't service

---

#### Mercury {#mercury}
##### ADSL

- Operating Mode: ADSL or ATM
- PPP Protocol: PPP over ATM (PPPoA)
- PPP Username: username@kinect.co.nz (Where username is replaced with your chosen username)
- PPP Password: pass123
- VPI: 0
- VCI: 100
- Multiplexing: VCMUX
- MTU: 1500

##### VDSL

- Operating Mode: VDSL or PTM
- PPP Protocol: PPP over Ethernet (PPPoE)
- PPP Username: username@kinect.co.nz (Where username is replaced with your chosen username)
- PPP Password: pass123
- PPP Mode: PAP
- PCP: 0
- VLAN or 802.1q: Enabled
- VLAN ID: 10
- VLAN Priority or 802.1p: 0
- MTU: 1500

##### FIBRE

[Standard Settings](#standard_settings)

##### VoIP

Not disclosed

---

#### One NZ {#one_nz}
##### ADSL

- Operating Mode: ADSL or ATM
- PPP Protocol: PPP over ATM (PPPoA)
- PPP Username: User
- PPP Password: User
- VPI: 0
- VCI: 100
- Primary (Preferred) DNS: 203.109.191.1
- Secondary DNS: 203.118.191.1

##### VDSL

- Operating Mode: VDSL or PTM
- Access Type: Dynamic IP, IPoE (IP over Ethernet), Automatic IP or DHCP
- VLAN or 802.1q: Enabled
- VLAN ID: 10
- VLAN Priority or 802.1p: 0
- MTU: 1500
- IP Protocal Version: IPv4 and IPv6 
- IPv4 Address Type: DHCP
- IPv6 Address Type: DHCP

##### FIBRE

- Operating Mode: Fibre or Ethernet WAN
- Connection Type: Dynamic IP, IPoE (IP over Ethernet), Automatic IP or DHCP
- VLAN or 802.1q: Enabled
- VLAN ID: 10
- VLAN Priority or 802.1p: 0
- MTU: 1500
- IP Protocal Version: IPv4 + IPv6
- IPv4 Address Type: DHCP
- IPv6 Address Type: DHCP

##### VoIP

Not Disclosed

---

#### Skinny {#skinny}
##### ADSL

- Operating Mode: ADSL or ATM
- PPP Protocol: PPP over ATM (PPPoA)
- PPP Username: user@skinny.co.nz
- PPP Password: password
- VPI: 0
- VCI: 100

##### VDSL

- Operating Mode: VDSL or PTM
- PPP Protocol: PPP over Ethernet (PPPoE)
- PPP Username: user@skinny.co.nz
- PPP Password: password
- VPI: 0
- VCI: 110
- VLAN or 802.1q: Enabled
- VLAN ID: 10
- VLAN Priority or 802.1p: 0
- MTU: 1500

##### FIBRE

- Operating Mode: Fibre or Ethernet WAN
- PPP Protocol: PPP over Ethernet (PPPoE)
- PPP Username: user@skinny.co.nz
- PPP Password: password
- MTU: 1500

##### VoIP

Doesn't service

---

#### Spark {#spark}
##### ADSL

- Operating Mode: ADSL or ATM
- PPP Protocol: PPP over ATM (PPPoA)
- PPP Username: user@spark.co.nz
- PPP Password: password
- Authentication Mode: PAP
- PPP Mode: Always On
- VPI: 0
- VCI: 100
- Multiplexing: VCMUX
- MTU: 1500

##### VDSL

- Operating Mode: VDSL or PTM
- PPP Protocol: PPP over Ethernet (PPPoE)
- PPP Username: user@spark.co.nz
- PPP Password: password
- Authentication Mode: PAP
- VLAN or 802.1q: Enabled
- VLAN ID: 10
- VLAN Priority or 802.1p: 0
- MTU: Auto or 1500

##### FIBRE

- Operating Mode: Fibre or Ethernet WAN
- PPP Protocol: PPP over Ethernet (PPPoE)
- PPP Username: user@spark.co.nz
- PPP Password: password
- PPP Mode: Always On
- Authentication Mode: PAP
- VLAN or 802.1q: Enabled
- VLAN ID: 10
- VLAN Priority or 802.1p: 0
- MTU: Auto or 1500

##### VoIP

---

#### Trustpower {#trustpower}
##### ADSL

- Operating Mode: ADSL or ATM
- PPP Protocol: PPP over ATM (PPPoA)
- PPP Username: username@kinect.co.nz (Where username is replaced with your chosen username)
- PPP Password: pass123
- VPI: 0
- VCI: 100
- Multiplexing: VCMUX
- VLAN Priority or 802.1p: 
- MTU: 1500

##### VDSL

- Operating Mode: VDSL or PTM
- PPP Protocol: PPP over Ethernet (PPPoE)
- PPP Username: username@kinect.co.nz (Where username is replaced with your chosen username)
- PPP Password: pass123
- PPP Mode: PAP
- PCP: 0
- VLAN or 802.1q: Enabled
- VLAN ID: 10
- VLAN Priority or 802.1p: 0
- MTU: 1500

##### FIBRE

[Standard Settings](#standard_settings)

##### VoIP

Not disclosed

---

