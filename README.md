# port-watcher

日本の港湾・沿岸ライブカメラを白地図上にプロットするダッシュボード。海上保安庁「[海の安全情報](https://www6.kaiho.mlit.go.jp/livecamera.html)」の MICS ライブカメラ網（全国 79 点）を地図から横断的に閲覧できます。

静的サイトなので GitHub Pages でそのまま動きます。

## 使い方

任意の HTTP サーバーで配信してください（`file://` だと一部ブラウザで `data.js` のキャッシュ挙動が安定しません）。

```bash
python -m http.server 5173
# → http://localhost:5173/
```

マーカーをクリックすると名前・管区・サムネイル画像（30 秒間隔で更新）が出ます。「ライブカメラを開く」ボタンで海保のカメラページが別タブで開きます（埋め込みは `X-Frame-Options: SAMEORIGIN` のため不可）。

## ファイル

| ファイル | 説明 |
|---|---|
| `index.html` | UI 本体（Leaflet + topojson-client、CDN ロード） |
| `data.js` | `cameras.json` と `japan.topojson` をブラウザ向けに焼き込んだもの。`build.py` で再生成 |
| `cameras.json` | 海上保安庁 MICS の `camportalAPI/camera/getlist` レスポンス |
| `japan.topojson` | 日本の輪郭（[dataofjapan/land](https://github.com/dataofjapan/land) より） |
| `build.py` | `data.js` の再生成スクリプト |

## データ更新

```bash
curl -sL "https://camera.mics.kaiho.mlit.go.jp/camportalAPI/camera/getlist" -o cameras.json
python build.py
```

## データ出典

- 海上保安庁 海の安全情報（MICS）ライブカメラ — カメラ位置・サムネイル・ストリーム
- dataofjapan/land — 日本の TopoJSON 輪郭
