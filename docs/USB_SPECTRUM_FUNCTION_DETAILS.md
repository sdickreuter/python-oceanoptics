
##### implement...

| Spectrometer | HS 480       | FS 12        | fmt  | pixels | extra     |
|:-------------|:-------------|:-------------|------|--------|-----------|
| QE65Pro      | 5 x 512 +1B  | 40 x 64 +1B  | _<h_ |   1280 | XOR with 0x80? flip 15
| QE65000      | 5 x 512 +1B  | 40 x 64 +1B  | _<H_ |   1280 | flip 15
| USB2000+     | 9 x 512 +1B  | 64 x 64 +1B  | _<h_ |   2048 |
| Torus        | 9 x 512 +1B  | 64 x 64 +1B  | _<h_ |   2048 | 
| HR2000+      | 8 x 512 +1B  | 64 x 64 +1B  | _<h_ |   2048 | XOR with 0x20 flip 13
| Apex         | 9 x 512 +1B  | 66 x 64 +1B  | _<h_ |   2068 |
| Maya         | 9 x 512 +1B  | 66 x 64 +1B  | _<h_ |   2068 | 
| Maya2000Pro  | 9 x 512 +1B  | 66 x 64 +1B  | _<h_ |   2068 | 
| USB4000      |15 x 512 +1B  |120 x 64 +1B  | _<h_ |   3840 | HS: 2k from EP6 then EP2 
| HR4000       |15 x 512 +1B  |120 x 64 +1B  | _<h_ |   3840 | HS: 2k from EP6 then EP2 


##### wont implement for now

| Spectrometer | HS 480       | FS 12        | fmt  | pixels | extra     |
|:-------------|:-------------|:-------------|------|--------|-----------|
| HR2000       | -            | 64 x 64 +1B  | _64lsb/64msb<h_ | | 
| Jaz          | 8 x 512      | 64 x 64      | _<h_ |        | 
| NIR          | -            | Np x 64 +1B  | _<h_ | 256/512| 
| NIRQuest     |Np x 512 +1B  | Np x 64 +1B  | _<h_ | 256/512| XOR 0x80? flip bit 15


##### pixels definitions

| Spectrometer | dark                   | optical active |
|:-------------|------------------------|----------------|
| QE65Pro      | [1024:1028, 1034:1038] | [0:1024]
| QE65000      | [0:10,1034:1044]      | [10:1034]   Pixels [1034:1280] are 0
| USB2000+     | [0:18]                 | [20:2048]
| Torus        | [0:18]                 | [20:2048]
| HR2000+      | [0:18]                 | [20:2048]
| Apex         | [1:4, 2064:2068]       | [10:2058]
| Maya2000     | [0:8, 2072:2080]       | [16:2064]
| Maya2000pro  | [1:4, 2064:2068]       | [10:2058]
| USB4000      | [6:19]                 | [22:3670]
| HR4000       | [6:19]                 | [22:3670]




