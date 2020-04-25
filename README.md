# rstudio

To run:
```
docker-compose -f docker-compose.yml build
docker-compose -f docker-compose.yml up
```

Then try the jupyterhub: http://localhost:8000

```
Admin User: rhea password: rhea
Other User: ganymede password: ganymede
Other User: io password: io
```

Access RStudio: http://localhost:8787
```
User: rstudio password: mypassword
```

Example how to use Rstudio:

```
python install

create new python file example.py:

import sys
print(sys.version)

#Not required
reticulate::repl_python()

#How to run python correctly. It will ask to install miniconda. Do not do it. It fails to install one dependency and mess up the things.
install.packages("reticulate")
library(reticulate)
conda_list()
use_condaenv('conda')
py_install("pandas")
use_python('/opt/conda/bin/python')
source_python('example.py')



install.packages("riem")
install.packages("tidyverse")
install.packages("magrittr")

library(riem)
library(dplyr)
library(magrittr)
fahrenheit_to_centigrade <- function(x) {
  (x-32) * 5/9
  }
#So we can use the data in here to find the nearest observation point for any particular shop
stations <- riem_stations(network = "GB__ASOS")
#try Heathrow
station <- "EGLL"
measures <- riem_measures(station = station, date_start = "2018-08-01", date_end = as.character(Sys.Date()))
#days from timestamps to facilitate grouping
measures$day <- as.Date(measures$valid)
measures_agg <- measures %>%
  group_by(day) %>%
  summarise(
    temp_max = fahrenheit_to_centigrade(max(tmpf)),
    temp_min = fahrenheit_to_centigrade(min(tmpf)))
saveRDS(measures_agg, file = "toy_weather_data")

write.csv(measures_agg, file = "toy_weather_data.csv" )
```


JupyterHub
Check available kernels:
```
ipython kernelspec list
```

Notebooks:

Python Notebook:
```
import csv
with open('toy_weather_data.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)


import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("toy_weather_data.csv")
df.plot(x ='day', y='temp_max',color='red')
plt.show()

```
R Notebook:

```
df <- readRDS("toy_weather_data")
plot(df$day, df$temp_max)
```

How to configure RStudio different environment per user:
https://csgillespie.github.io/efficientR/3-3-r-startup.html#rprofile

```
file.edit("~/.Rprofile")

options(width=65, digits=5)
options(show.signif.stars=FALSE)
setHook(packageEvent("grDevices", "onLoad"),
        function(...) grDevices::ps.options(horizontal=FALSE))
set.seed(1234)
#.First <- function() cat("\n   Welcome to R!\n\n")
#.Last <- function()  cat("\n   Goodbye!\n\n")

file.edit("~/.Renviron")

R_LIBS=/home/rhea/R/library
PAGER=/usr/local/bin/less


myPaths <- .libPaths()
myPaths <- c(myPaths, ‘/home/rhea/R/library’)
.libPaths(myPaths)  # add new path
```

Adding users in Rstudio.
```
useradd -m -G staff -p $(openssl passwd -1 rhea) rhea
mkdir -p /home/rhea/R/library
```

Run Jupyter easy:

```
docker run -d -p 8000:8000 --name jupyterhub jupyterhub/jupyterhub jupyterhub
docker exec -t $container bash
```

```
root@ae7d04b7ecba:/srv/jupyterhub# username="admin"
root@ae7d04b7ecba:/srv/jupyterhub# password="admin"
root@ae7d04b7ecba:/srv/jupyterhub# useradd -m -p $(openssl passwd -1 ${password}) -s /bin/bash -G sudo ${username}
```


https://github.com/michhar/custom-jupyterhub-linux-vm/blob/0e7658620156eef5f0e89973a76cddde39385f73/archive/ForUnix_py36.dockerfile
