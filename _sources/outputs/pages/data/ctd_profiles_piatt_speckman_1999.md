---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.5
---

```{code-cell}
:tags: [remove-input]

import intake
import ciofs_hindcast_report as chr
import hvplot.pandas  # noqa
import ocean_model_skill_assessor as omsa
import pandas as pd
import cmocean.cm as cmo
import holoviews as hv
from holoviews import opts
```

(page:ctd_profiles_piatt_speckman_1999)=
# CTD Profiles (Piatt Speckman)

* Piatt Speckman 1995-99
* ctd_profiles_piatt_speckman_1999
* One-off CTD profiles April to September 1999

CTD Profiles in Cook Inlet



```{dropdown} Dataset metadata

|     | Dataset   | featuretype   | key_variables    |   maxLatitude |   maxLongitude | maxTime             |   minLatitude |   minLongitude | minTime             | urlpath                                                    |
|----:|:----------|:--------------|:-----------------|--------------:|---------------:|:--------------------|--------------:|---------------:|:--------------------|:-----------------------------------------------------------|
|   0 | 10159900  | profile       | ['temp', 'salt'] |       59.6413 |       -151.36  | 1999-08-26 17:51:00 |       59.6413 |       -151.36  | 1999-08-26 17:51:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|   1 | 10159901  | profile       | ['temp', 'salt'] |       59.6205 |       -151.351 | 1999-08-26 18:01:00 |       59.6205 |       -151.351 | 1999-08-26 18:01:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|   2 | 10159902  | profile       | ['temp', 'salt'] |       59.5952 |       -151.349 | 1999-08-26 18:12:00 |       59.5952 |       -151.349 | 1999-08-26 18:12:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|   3 | 10159903  | profile       | ['temp', 'salt'] |       59.5807 |       -151.341 | 1999-08-26 18:33:00 |       59.5807 |       -151.341 | 1999-08-26 18:33:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|   4 | 10159904  | profile       | ['temp', 'salt'] |       59.5712 |       -151.336 | 1999-08-26 18:41:00 |       59.5712 |       -151.336 | 1999-08-26 18:41:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|   5 | 10159905  | profile       | ['temp', 'salt'] |       59.6217 |       -151.626 | 1999-08-26 19:16:00 |       59.6217 |       -151.626 | 1999-08-26 19:16:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|   6 | 10159907  | profile       | ['temp', 'salt'] |       59.5733 |       -151.599 | 1999-08-26 19:28:00 |       59.5733 |       -151.599 | 1999-08-26 19:28:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|   7 | 10159908  | profile       | ['temp', 'salt'] |       59.5532 |       -151.589 | 1999-08-26 19:38:00 |       59.5532 |       -151.589 | 1999-08-26 19:38:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|   8 | 10159909  | profile       | ['temp', 'salt'] |       59.519  |       -151.581 | 1999-08-26 19:54:00 |       59.519  |       -151.581 | 1999-08-26 19:54:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|   9 | 10159910  | profile       | ['temp', 'salt'] |       59.4895 |       -151.582 | 1999-08-26 20:04:00 |       59.4895 |       -151.582 | 1999-08-26 20:04:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  10 | 10159911  | profile       | ['temp', 'salt'] |       59.4853 |       -151.577 | 1999-08-28 12:16:00 |       59.4853 |       -151.577 | 1999-08-28 12:16:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  11 | 10159913  | profile       | ['temp', 'salt'] |       59.6202 |       -151.349 | 1999-08-30 11:47:00 |       59.6202 |       -151.349 | 1999-08-30 11:47:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  12 | 10159914  | profile       | ['temp', 'salt'] |       59.5132 |       -151.476 | 1999-08-30 12:43:00 |       59.5132 |       -151.476 | 1999-08-30 12:43:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  13 | 10159915  | profile       | ['temp', 'salt'] |       59.62   |       -151.351 | 1999-09-13 15:20:00 |       59.62   |       -151.351 | 1999-09-13 15:20:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  14 | 10159916  | profile       | ['temp', 'salt'] |       59.5135 |       -151.478 | 1999-09-13 16:17:00 |       59.5135 |       -151.478 | 1999-09-13 16:17:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  15 | 9051600   | profile       | ['temp', 'salt'] |       59.5122 |       -151.48  | 1999-04-26 15:30:00 |       59.5122 |       -151.48  | 1999-04-26 15:30:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  16 | 9051601   | profile       | ['temp', 'salt'] |       59.6188 |       -151.351 | 1999-04-26 17:00:00 |       59.6188 |       -151.351 | 1999-04-26 17:00:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  17 | 9051602   | profile       | ['temp', 'salt'] |       59.6233 |       -151.626 | 1999-04-27 09:45:00 |       59.6233 |       -151.626 | 1999-04-27 09:45:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  18 | 9051603   | profile       | ['temp', 'salt'] |       59.5818 |       -151.602 | 1999-04-27 10:00:00 |       59.5818 |       -151.602 | 1999-04-27 10:00:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  19 | 9051604   | profile       | ['temp', 'salt'] |       59.5535 |       -151.591 | 1999-04-27 10:10:00 |       59.5535 |       -151.591 | 1999-04-27 10:10:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  20 | 9051605   | profile       | ['temp', 'salt'] |       59.5192 |       -151.583 | 1999-04-27 10:28:00 |       59.5192 |       -151.583 | 1999-04-27 10:28:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  21 | 9051606   | profile       | ['temp', 'salt'] |       59.4895 |       -151.581 | 1999-04-27 10:43:00 |       59.4895 |       -151.581 | 1999-04-27 10:43:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  22 | 9051607   | profile       | ['temp', 'salt'] |       59.4857 |       -151.576 | 1999-04-27 10:50:00 |       59.4857 |       -151.576 | 1999-04-27 10:50:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  23 | 9051608   | profile       | ['temp', 'salt'] |       59.5717 |       -151.336 | 1999-04-27 11:30:00 |       59.5717 |       -151.336 | 1999-04-27 11:30:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  24 | 9051609   | profile       | ['temp', 'salt'] |       59.58   |       -151.34  | 1999-04-27 11:35:00 |       59.58   |       -151.34  | 1999-04-27 11:35:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  25 | 9051610   | profile       | ['temp', 'salt'] |       59.595  |       -151.351 | 1999-04-27 11:45:00 |       59.595  |       -151.351 | 1999-04-27 11:45:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  26 | 9051611   | profile       | ['temp', 'salt'] |       59.62   |       -151.351 | 1999-04-27 12:05:00 |       59.62   |       -151.351 | 1999-04-27 12:05:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  27 | 9051612   | profile       | ['temp', 'salt'] |       59.5753 |       -151.361 | 1999-04-27 12:16:00 |       59.5753 |       -151.361 | 1999-04-27 12:16:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  28 | 9051613   | profile       | ['temp', 'salt'] |       59.62   |       -151.351 | 1999-05-05 16:50:00 |       59.62   |       -151.351 | 1999-05-05 16:50:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  29 | 9051614   | profile       | ['temp', 'salt'] |       59.6197 |       -151.35  | 1999-05-05 18:44:00 |       59.6197 |       -151.35  | 1999-05-05 18:44:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  30 | 9051615   | profile       | ['temp', 'salt'] |       59.5132 |       -151.477 | 1999-05-11 10:08:00 |       59.5132 |       -151.477 | 1999-05-11 10:08:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  31 | 9051616   | profile       | ['temp', 'salt'] |       59.6197 |       -151.35  | 1999-05-11 12:30:00 |       59.6197 |       -151.35  | 1999-05-11 12:30:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  32 | 9060400   | profile       | ['temp', 'salt'] |       59.5122 |       -151.48  | 1999-05-23 16:40:00 |       59.5122 |       -151.48  | 1999-05-23 16:40:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  33 | 9060401   | profile       | ['temp', 'salt'] |       59.6203 |       -151.351 | 1999-05-23 18:09:00 |       59.6203 |       -151.351 | 1999-05-23 18:09:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  34 | 9060402   | profile       | ['temp', 'salt'] |       59.5122 |       -151.48  | 1999-05-28 17:20:00 |       59.5122 |       -151.48  | 1999-05-28 17:20:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  35 | 9060403   | profile       | ['temp', 'salt'] |       59.6203 |       -151.351 | 1999-05-28 19:13:00 |       59.6203 |       -151.351 | 1999-05-28 19:13:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  36 | 9060404   | profile       | ['temp', 'salt'] |       59.622  |       -151.627 | 1999-06-01 16:46:00 |       59.622  |       -151.627 | 1999-06-01 16:46:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  37 | 9060405   | profile       | ['temp', 'salt'] |       59.5818 |       -151.602 | 1999-06-01 17:02:00 |       59.5818 |       -151.602 | 1999-06-01 17:02:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  38 | 9060406   | profile       | ['temp', 'salt'] |       59.5535 |       -151.591 | 1999-06-01 17:19:00 |       59.5535 |       -151.591 | 1999-06-01 17:19:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  39 | 9060407   | profile       | ['temp', 'salt'] |       59.5192 |       -151.583 | 1999-06-01 17:36:00 |       59.5192 |       -151.583 | 1999-06-01 17:36:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  40 | 9060408   | profile       | ['temp', 'salt'] |       59.4895 |       -151.582 | 1999-06-01 17:51:00 |       59.4895 |       -151.582 | 1999-06-01 17:51:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  41 | 9060409   | profile       | ['temp', 'salt'] |       59.4853 |       -151.577 | 1999-06-01 17:59:00 |       59.4853 |       -151.577 | 1999-06-01 17:59:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  42 | 9060410   | profile       | ['temp', 'salt'] |       59.5713 |       -151.336 | 1999-06-01 18:44:00 |       59.5713 |       -151.336 | 1999-06-01 18:44:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  43 | 9060411   | profile       | ['temp', 'salt'] |       59.5807 |       -151.341 | 1999-06-01 18:50:00 |       59.5807 |       -151.341 | 1999-06-01 18:50:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  44 | 9060412   | profile       | ['temp', 'salt'] |       59.595  |       -151.351 | 1999-06-01 19:00:00 |       59.595  |       -151.351 | 1999-06-01 19:00:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  45 | 9060413   | profile       | ['temp', 'salt'] |       59.6205 |       -151.352 | 1999-06-01 19:17:00 |       59.6205 |       -151.352 | 1999-06-01 19:17:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  46 | 9060414   | profile       | ['temp', 'salt'] |       59.5753 |       -151.361 | 1999-06-01 19:29:00 |       59.5753 |       -151.361 | 1999-06-01 19:29:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  47 | 9060415   | profile       | ['temp', 'salt'] |       59.6203 |       -151.351 | 1999-06-04 12:06:00 |       59.6203 |       -151.351 | 1999-06-04 12:06:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  48 | 9060415b  | profile       | ['temp', 'salt'] |       59.5132 |       -151.476 | 1999-06-05 09:00:00 |       59.5132 |       -151.476 | 1999-06-05 09:00:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  49 | 9063000   | profile       | ['temp', 'salt'] |       59.6203 |       -151.351 | 1999-06-29 13:04:00 |       59.6203 |       -151.351 | 1999-06-29 13:04:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  50 | 9063001   | profile       | ['temp', 'salt'] |       59.5127 |       -151.477 | 1999-06-29 14:45:00 |       59.5127 |       -151.477 | 1999-06-29 14:45:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  51 | 9063002   | profile       | ['temp', 'salt'] |       59.6088 |       -153.165 | 1999-06-30 12:52:00 |       59.6088 |       -153.165 | 1999-06-30 12:52:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  52 | 9063003   | profile       | ['temp', 'salt'] |       59.6102 |       -153.046 | 1999-06-30 13:24:00 |       59.6102 |       -153.046 | 1999-06-30 13:24:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  53 | 9063004   | profile       | ['temp', 'salt'] |       59.6083 |       -152.928 | 1999-06-30 13:45:00 |       59.6083 |       -152.928 | 1999-06-30 13:45:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  54 | 9063005   | profile       | ['temp', 'salt'] |       59.6088 |       -152.808 | 1999-06-30 14:12:00 |       59.6088 |       -152.808 | 1999-06-30 14:12:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  55 | 9063006   | profile       | ['temp', 'salt'] |       59.6098 |       -152.689 | 1999-06-30 14:43:00 |       59.6098 |       -152.689 | 1999-06-30 14:43:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  56 | 9063007   | profile       | ['temp', 'salt'] |       59.6098 |       -152.572 | 1999-06-30 15:25:00 |       59.6098 |       -152.572 | 1999-06-30 15:25:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  57 | 9063008   | profile       | ['temp', 'salt'] |       59.6117 |       -152.45  | 1999-06-30 16:01:00 |       59.6117 |       -152.45  | 1999-06-30 16:01:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  58 | 9063009   | profile       | ['temp', 'salt'] |       59.609  |       -152.332 | 1999-06-30 16:29:00 |       59.609  |       -152.332 | 1999-06-30 16:29:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  59 | 9063010   | profile       | ['temp', 'salt'] |       59.613  |       -152.213 | 1999-06-30 17:00:00 |       59.613  |       -152.213 | 1999-06-30 17:00:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  60 | 9063011   | profile       | ['temp', 'salt'] |       59.6093 |       -152.094 | 1999-06-30 17:26:00 |       59.6093 |       -152.094 | 1999-06-30 17:26:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  61 | 9063012   | profile       | ['temp', 'salt'] |       59.6082 |       -151.973 | 1999-06-30 17:52:00 |       59.6082 |       -151.973 | 1999-06-30 17:52:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  62 | 9063013   | profile       | ['temp', 'salt'] |       59.608  |       -151.856 | 1999-06-30 18:19:00 |       59.608  |       -151.856 | 1999-06-30 18:19:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  63 | 9063014   | profile       | ['temp', 'salt'] |       59.6077 |       -151.82  | 1999-06-30 18:43:00 |       59.6077 |       -151.82  | 1999-06-30 18:43:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  64 | 9063015   | profile       | ['temp', 'salt'] |       59.6158 |       -151.616 | 1999-06-30 19:07:00 |       59.6158 |       -151.616 | 1999-06-30 19:07:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  65 | 9072201   | profile       | ['temp', 'salt'] |       59.4888 |       -151.58  | 1999-07-14 13:20:00 |       59.4888 |       -151.58  | 1999-07-14 13:20:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  66 | 9072202   | profile       | ['temp', 'salt'] |       59.5181 |       -151.581 | 1999-07-14 13:36:00 |       59.5181 |       -151.581 | 1999-07-14 13:36:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  67 | 9072203   | profile       | ['temp', 'salt'] |       59.5538 |       -151.591 | 1999-07-14 13:50:00 |       59.5538 |       -151.591 | 1999-07-14 13:50:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  68 | 9072204   | profile       | ['temp', 'salt'] |       59.5818 |       -151.599 | 1999-07-14 14:04:00 |       59.5818 |       -151.599 | 1999-07-14 14:04:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  69 | 9072205   | profile       | ['temp', 'salt'] |       59.622  |       -151.627 | 1999-07-14 14:18:00 |       59.622  |       -151.627 | 1999-07-14 14:18:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  70 | 9072206   | profile       | ['temp', 'salt'] |       59.5713 |       -151.336 | 1999-07-14 14:52:00 |       59.5713 |       -151.336 | 1999-07-14 14:52:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  71 | 9072207   | profile       | ['temp', 'salt'] |       59.58   |       -151.339 | 1999-07-14 14:58:00 |       59.58   |       -151.339 | 1999-07-14 14:58:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  72 | 9072208   | profile       | ['temp', 'salt'] |       59.595  |       -151.35  | 1999-07-14 15:07:00 |       59.595  |       -151.35  | 1999-07-14 15:07:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  73 | 9072209   | profile       | ['temp', 'salt'] |       59.6205 |       -151.352 | 1999-07-14 15:23:00 |       59.6205 |       -151.352 | 1999-07-14 15:23:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  74 | 9072210   | profile       | ['temp', 'salt'] |       59.6425 |       -151.361 | 1999-07-14 15:34:00 |       59.6425 |       -151.361 | 1999-07-14 15:34:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  75 | 9072211   | profile       | ['temp', 'salt'] |       59.6198 |       -151.35  | 1999-07-17 13:27:00 |       59.6198 |       -151.35  | 1999-07-17 13:27:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  76 | 9072212   | profile       | ['temp', 'salt'] |       59.5123 |       -151.478 | 1999-07-17 14:57:00 |       59.5123 |       -151.478 | 1999-07-17 14:57:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  77 | 9072213   | profile       | ['temp', 'salt'] |       59.62   |       -151.35  | 1999-07-17 11:17:00 |       59.62   |       -151.35  | 1999-07-17 11:17:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  78 | 9072214   | profile       | ['temp', 'salt'] |       59.5125 |       -151.479 | 1999-07-17 12:47:00 |       59.5125 |       -151.479 | 1999-07-17 12:47:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  79 | 90729a00  | profile       | ['temp', 'salt'] |       59.5    |       -151.972 | 1999-07-25 14:12:00 |       59.5    |       -151.972 | 1999-07-25 14:12:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  80 | 90729a01  | profile       | ['temp', 'salt'] |       59.3448 |       -152.252 | 1999-07-26 14:05:00 |       59.3448 |       -152.252 | 1999-07-26 14:05:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  81 | 90729a02  | profile       | ['temp', 'salt'] |       59.2543 |       -152.318 | 1999-07-26 16:29:00 |       59.2543 |       -152.318 | 1999-07-26 16:29:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  82 | 90729a03  | profile       | ['temp', 'salt'] |       59.2374 |       -151.966 | 1999-07-26 17:59:00 |       59.2374 |       -151.966 | 1999-07-26 17:59:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  83 | 90729a04  | profile       | ['temp', 'salt'] |       59.187  |       -151.969 | 1999-07-26 18:26:00 |       59.187  |       -151.969 | 1999-07-26 18:26:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  84 | 90729a05  | profile       | ['temp', 'salt'] |       59.1303 |       -151.968 | 1999-07-26 18:58:00 |       59.1303 |       -151.968 | 1999-07-26 18:58:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  85 | 90729a06  | profile       | ['temp', 'salt'] |       59.0628 |       -151.963 | 1999-07-26 19:42:00 |       59.0628 |       -151.963 | 1999-07-26 19:42:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  86 | 90729a07  | profile       | ['temp', 'salt'] |       58.9967 |       -151.961 | 1999-07-26 20:20:00 |       58.9967 |       -151.961 | 1999-07-26 20:20:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  87 | 90729a08  | profile       | ['temp', 'salt'] |       58.934  |       -151.958 | 1999-07-26 20:54:00 |       58.934  |       -151.958 | 1999-07-26 20:54:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  88 | 90729a09  | profile       | ['temp', 'salt'] |       59.185  |       -151.496 | 1999-07-27 15:39:00 |       59.185  |       -151.496 | 1999-07-27 15:39:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  89 | 90729a10  | profile       | ['temp', 'salt'] |       59.1122 |       -151.608 | 1999-07-27 18:20:00 |       59.1122 |       -151.608 | 1999-07-27 18:20:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  90 | 90729a11  | profile       | ['temp', 'salt'] |       59.1364 |       -151.719 | 1999-07-28 16:14:00 |       59.1364 |       -151.719 | 1999-07-28 16:14:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  91 | 90729a12  | profile       | ['temp', 'salt'] |       59.1385 |       -151.639 | 1999-07-28 17:42:00 |       59.1385 |       -151.639 | 1999-07-28 17:42:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  92 | 90729a13  | profile       | ['temp', 'salt'] |       59.1541 |       -151.569 | 1999-07-28 19:36:00 |       59.1541 |       -151.569 | 1999-07-28 19:36:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  93 | 90729a14  | profile       | ['temp', 'salt'] |       58.9131 |       -151.742 | 1999-07-29 09:06:00 |       58.9131 |       -151.742 | 1999-07-29 09:06:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  94 | 9082101   | profile       | ['temp', 'salt'] |       59.6205 |       -151.35  | 1999-08-16 17:38:00 |       59.6205 |       -151.35  | 1999-08-16 17:38:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  95 | 9082102   | profile       | ['temp', 'salt'] |       59.4685 |       -151.745 | 1999-08-17 10:42:00 |       59.4685 |       -151.745 | 1999-08-17 10:42:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  96 | 9082103   | profile       | ['temp', 'salt'] |       59.4532 |       -151.726 | 1999-08-17 12:03:00 |       59.4532 |       -151.726 | 1999-08-17 12:03:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  97 | 9082104   | profile       | ['temp', 'salt'] |       59.4551 |       -151.754 | 1999-08-17 12:30:00 |       59.4551 |       -151.754 | 1999-08-17 12:30:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  98 | 9082106   | profile       | ['temp', 'salt'] |       59.475  |       -151.781 | 1999-08-17 13:30:00 |       59.475  |       -151.781 | 1999-08-17 13:30:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
|  99 | 9082107   | profile       | ['temp', 'salt'] |       59.554  |       -151.396 | 1999-08-17 14:56:00 |       59.554  |       -151.396 | 1999-08-17 14:56:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
| 100 | 9082108   | profile       | ['temp', 'salt'] |       59.5595 |       -151.378 | 1999-08-17 15:18:00 |       59.5595 |       -151.378 | 1999-08-17 15:18:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
| 101 | 9082109   | profile       | ['temp', 'salt'] |       59.5554 |       -151.404 | 1999-08-17 15:55:00 |       59.5554 |       -151.404 | 1999-08-17 15:55:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
| 102 | 9082110   | profile       | ['temp', 'salt'] |       59.5617 |       -151.38  | 1999-08-17 16:34:00 |       59.5617 |       -151.38  | 1999-08-17 16:34:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
| 103 | 9082111   | profile       | ['temp', 'salt'] |       59.618  |       -151.196 | 1999-08-20 10:59:00 |       59.618  |       -151.196 | 1999-08-20 10:59:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
| 104 | 9082112   | profile       | ['temp', 'salt'] |       59.6083 |       -151.194 | 1999-08-20 11:11:00 |       59.6083 |       -151.194 | 1999-08-20 11:11:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
| 105 | 9082113   | profile       | ['temp', 'salt'] |       59.5804 |       -151.33  | 1999-08-20 12:43:00 |       59.5804 |       -151.33  | 1999-08-20 12:43:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
| 106 | 9082114   | profile       | ['temp', 'salt'] |       59.5798 |       -151.313 | 1999-08-20 12:52:00 |       59.5798 |       -151.313 | 1999-08-20 12:52:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
| 107 | 9082115   | profile       | ['temp', 'salt'] |       59.5781 |       -151.294 | 1999-08-20 13:32:00 |       59.5781 |       -151.294 | 1999-08-20 13:32:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
| 108 | 9082116   | profile       | ['temp', 'salt'] |       59.5235 |       -151.447 | 1999-08-20 15:20:00 |       59.5235 |       -151.447 | 1999-08-20 15:20:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
| 109 | 9082117   | profile       | ['temp', 'salt'] |       59.4778 |       -151.492 | 1999-08-20 15:37:00 |       59.4778 |       -151.492 | 1999-08-20 15:37:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
| 110 | 9082118   | profile       | ['temp', 'salt'] |       59.4839 |       -151.583 | 1999-08-21 09:28:00 |       59.4839 |       -151.583 | 1999-08-21 09:28:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
| 111 | 9082119   | profile       | ['temp', 'salt'] |       59.4903 |       -151.608 | 1999-08-21 10:36:00 |       59.4903 |       -151.608 | 1999-08-21 10:36:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
| 112 | 9082120   | profile       | ['temp', 'salt'] |       59.4929 |       -151.609 | 1999-08-21 11:36:00 |       59.4929 |       -151.609 | 1999-08-21 11:36:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
| 113 | 9082121   | profile       | ['temp', 'salt'] |       59.4977 |       -151.633 | 1999-08-21 12:38:00 |       59.4977 |       -151.633 | 1999-08-21 12:38:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
| 114 | 9082122   | profile       | ['temp', 'salt'] |       59.4886 |       -151.638 | 1999-08-21 13:40:00 |       59.4886 |       -151.638 | 1999-08-21 13:40:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |
| 115 | 9082123   | profile       | ['temp', 'salt'] |       59.5032 |       -151.631 | 1999-08-21 14:41:00 |       59.5032 |       -151.631 | 1999-08-21 14:41:00 | https://researchworkspace.com/files/42400652/Piatt1999.csv |

```



```{code-cell}
:tags: [remove-input]

cat = intake.open_catalog(chr.CAT_NAME("ctd_profiles_piatt_speckman_1999"))
```

## Map of CTD Profiles
    

```{code-cell}
:tags: [remove-input]

getattr(chr.src.plot_dataset_on_map, "ctd_profiles_piatt_speckman_1999")("ctd_profiles_piatt_speckman_1999")
```

## 10159900
        

```{code-cell}
:tags: [full-width, remove-input]

cat['10159900'].plot.data()
```

## 10159901
        

```{code-cell}
:tags: [full-width, remove-input]

cat['10159901'].plot.data()
```

## 10159902
        

```{code-cell}
:tags: [full-width, remove-input]

cat['10159902'].plot.data()
```

## 10159903
        

```{code-cell}
:tags: [full-width, remove-input]

cat['10159903'].plot.data()
```

## 10159904
        

```{code-cell}
:tags: [full-width, remove-input]

cat['10159904'].plot.data()
```

## 10159905
        

```{code-cell}
:tags: [full-width, remove-input]

cat['10159905'].plot.data()
```

## 10159907
        

```{code-cell}
:tags: [full-width, remove-input]

cat['10159907'].plot.data()
```

## 10159908
        

```{code-cell}
:tags: [full-width, remove-input]

cat['10159908'].plot.data()
```

## 10159909
        

```{code-cell}
:tags: [full-width, remove-input]

cat['10159909'].plot.data()
```

## 10159910
        

```{code-cell}
:tags: [full-width, remove-input]

cat['10159910'].plot.data()
```

## 10159911
        

```{code-cell}
:tags: [full-width, remove-input]

cat['10159911'].plot.data()
```

## 10159913
        

```{code-cell}
:tags: [full-width, remove-input]

cat['10159913'].plot.data()
```

## 10159914
        

```{code-cell}
:tags: [full-width, remove-input]

cat['10159914'].plot.data()
```

## 10159915
        

```{code-cell}
:tags: [full-width, remove-input]

cat['10159915'].plot.data()
```

## 10159916
        

```{code-cell}
:tags: [full-width, remove-input]

cat['10159916'].plot.data()
```

## 9051600
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9051600'].plot.data()
```

## 9051601
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9051601'].plot.data()
```

## 9051602
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9051602'].plot.data()
```

## 9051603
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9051603'].plot.data()
```

## 9051604
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9051604'].plot.data()
```

## 9051605
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9051605'].plot.data()
```

## 9051606
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9051606'].plot.data()
```

## 9051607
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9051607'].plot.data()
```

## 9051608
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9051608'].plot.data()
```

## 9051609
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9051609'].plot.data()
```

## 9051610
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9051610'].plot.data()
```

## 9051611
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9051611'].plot.data()
```

## 9051612
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9051612'].plot.data()
```

## 9051613
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9051613'].plot.data()
```

## 9051614
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9051614'].plot.data()
```

## 9051615
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9051615'].plot.data()
```

## 9051616
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9051616'].plot.data()
```

## 9060400
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9060400'].plot.data()
```

## 9060401
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9060401'].plot.data()
```

## 9060402
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9060402'].plot.data()
```

## 9060403
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9060403'].plot.data()
```

## 9060404
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9060404'].plot.data()
```

## 9060405
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9060405'].plot.data()
```

## 9060406
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9060406'].plot.data()
```

## 9060407
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9060407'].plot.data()
```

## 9060408
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9060408'].plot.data()
```

## 9060409
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9060409'].plot.data()
```

## 9060410
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9060410'].plot.data()
```

## 9060411
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9060411'].plot.data()
```

## 9060412
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9060412'].plot.data()
```

## 9060413
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9060413'].plot.data()
```

## 9060414
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9060414'].plot.data()
```

## 9060415
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9060415'].plot.data()
```

## 9060415b
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9060415b'].plot.data()
```

## 9063000
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9063000'].plot.data()
```

## 9063001
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9063001'].plot.data()
```

## 9063002
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9063002'].plot.data()
```

## 9063003
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9063003'].plot.data()
```

## 9063004
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9063004'].plot.data()
```

## 9063005
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9063005'].plot.data()
```

## 9063006
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9063006'].plot.data()
```

## 9063007
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9063007'].plot.data()
```

## 9063008
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9063008'].plot.data()
```

## 9063009
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9063009'].plot.data()
```

## 9063010
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9063010'].plot.data()
```

## 9063011
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9063011'].plot.data()
```

## 9063012
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9063012'].plot.data()
```

## 9063013
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9063013'].plot.data()
```

## 9063014
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9063014'].plot.data()
```

## 9063015
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9063015'].plot.data()
```

## 9072201
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9072201'].plot.data()
```

## 9072202
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9072202'].plot.data()
```

## 9072203
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9072203'].plot.data()
```

## 9072204
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9072204'].plot.data()
```

## 9072205
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9072205'].plot.data()
```

## 9072206
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9072206'].plot.data()
```

## 9072207
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9072207'].plot.data()
```

## 9072208
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9072208'].plot.data()
```

## 9072209
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9072209'].plot.data()
```

## 9072210
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9072210'].plot.data()
```

## 9072211
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9072211'].plot.data()
```

## 9072212
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9072212'].plot.data()
```

## 9072213
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9072213'].plot.data()
```

## 9072214
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9072214'].plot.data()
```

## 90729a00
        

```{code-cell}
:tags: [full-width, remove-input]

cat['90729a00'].plot.data()
```

## 90729a01
        

```{code-cell}
:tags: [full-width, remove-input]

cat['90729a01'].plot.data()
```

## 90729a02
        

```{code-cell}
:tags: [full-width, remove-input]

cat['90729a02'].plot.data()
```

## 90729a03
        

```{code-cell}
:tags: [full-width, remove-input]

cat['90729a03'].plot.data()
```

## 90729a04
        

```{code-cell}
:tags: [full-width, remove-input]

cat['90729a04'].plot.data()
```

## 90729a05
        

```{code-cell}
:tags: [full-width, remove-input]

cat['90729a05'].plot.data()
```

## 90729a06
        

```{code-cell}
:tags: [full-width, remove-input]

cat['90729a06'].plot.data()
```

## 90729a07
        

```{code-cell}
:tags: [full-width, remove-input]

cat['90729a07'].plot.data()
```

## 90729a08
        

```{code-cell}
:tags: [full-width, remove-input]

cat['90729a08'].plot.data()
```

## 90729a09
        

```{code-cell}
:tags: [full-width, remove-input]

cat['90729a09'].plot.data()
```

## 90729a10
        

```{code-cell}
:tags: [full-width, remove-input]

cat['90729a10'].plot.data()
```

## 90729a11
        

```{code-cell}
:tags: [full-width, remove-input]

cat['90729a11'].plot.data()
```

## 90729a12
        

```{code-cell}
:tags: [full-width, remove-input]

cat['90729a12'].plot.data()
```

## 90729a13
        

```{code-cell}
:tags: [full-width, remove-input]

cat['90729a13'].plot.data()
```

## 90729a14
        

```{code-cell}
:tags: [full-width, remove-input]

cat['90729a14'].plot.data()
```

## 9082101
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9082101'].plot.data()
```

## 9082102
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9082102'].plot.data()
```

## 9082103
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9082103'].plot.data()
```

## 9082104
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9082104'].plot.data()
```

## 9082106
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9082106'].plot.data()
```

## 9082107
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9082107'].plot.data()
```

## 9082108
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9082108'].plot.data()
```

## 9082109
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9082109'].plot.data()
```

## 9082110
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9082110'].plot.data()
```

## 9082111
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9082111'].plot.data()
```

## 9082112
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9082112'].plot.data()
```

## 9082113
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9082113'].plot.data()
```

## 9082114
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9082114'].plot.data()
```

## 9082115
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9082115'].plot.data()
```

## 9082116
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9082116'].plot.data()
```

## 9082117
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9082117'].plot.data()
```

## 9082118
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9082118'].plot.data()
```

## 9082119
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9082119'].plot.data()
```

## 9082120
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9082120'].plot.data()
```

## 9082121
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9082121'].plot.data()
```

## 9082122
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9082122'].plot.data()
```

## 9082123
        

```{code-cell}
:tags: [full-width, remove-input]

cat['9082123'].plot.data()
```
