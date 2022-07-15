# ixnetwork-graphana
a sample of how to put IxNetwork stats in a Graphana dashboard

```
pacman -Syu
pacman -S docker-compose

git clone https://github.com/mgheorghe/ixnetwork-graphana.git
```

download `https://support.ixiacom.com/version/ixnetwork-920` `IxNetwork Web Edition - Docker deployment`
copy the `Ixia_IxNetworkWeb_Docker_9.20.2112.27.tar.bz2` in `ixnetwork-graphana` folder

```

cd ixnetwork-graphana
docker-compose up -d
```