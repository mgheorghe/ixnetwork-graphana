# ixnetwork-graphana
a sample of how to put IxNetwork stats in a Graphana dashboard

```
pacman -Syu
pacman -S docker-compose

git clone https://github.com/mgheorghe/ixnetwork-graphana.git

cd ixnetwork-graphana
```

download `https://support.ixiacom.com/version/ixnetwork-1040` `IxNetwork Web Edition - Docker deployment`
copy the `Ixia_IxNetworkWeb_Docker_10.40.2406.91.tar.bz2` in `ixnetwork-graphana` folder

```
tar xjf ./Ixia_IxNetworkWeb_Docker_10.40.2406.91.tar.bz2
docker load -i ./Ixia_IxNetworkWeb_Docker_10.40.2406.91.tar
 
docker compose up -d

docker compose stop
```
![dashboard](display.jpg)
