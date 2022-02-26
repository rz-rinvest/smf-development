from Assets import AssetManager

am = AssetManager.AM()

ast = am.GetActiveAssets()

for asset in ast:
  print(asset.name)

