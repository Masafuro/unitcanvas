# UnitCanvas & Webfont Tools

HTML要素をキャンバスのように自由に配置する `UnitCanvas` レイアウトシステムと、日本語フォントを最適化するサブセット化ツールのプロジェクトです。

## 概要

このプロジェクトは、主に2つの機能を提供します。

1.  **UnitCanvas**: CSSの絶対座標を使って、HTML要素をピクセル単位で正確に配置する軽量なレイアウト手法です。
2.  **Webフォント最適化**: HTMLで実際に使用されている文字だけを抽出した、軽量なWebフォント（サブセットフォント）を自動生成します。

デザイナーやコンテンツ編集者は、HTMLと簡単なコマンド操作で、デザインの適用やプレビューが可能です。

## 使い方

### 1. プレビューする

`index.html` の表示をブラウザで確認します。

```bash
python preview.py --serve
```

### 2. テキストにフォントを適用する

`index.html` を編集し、フォントを適用したいHTML要素の `class` に `f_フォント名` を追加します。フォント名は `fonts` フォルダにあるファイル名と一致させます。

**例:** `ZenOldMincho-Black.ttf` を使いたい場合

```html
<div class="f_ZenOldMincho-Black">このテキストにフォントが適用されます</div>
```

### 3. Webフォントを生成する

`index.html` で使用した文字をもとに、`subfonts` フォルダに最適化されたフォントファイル (`.woff2`, `.woff`) を生成します。

```bash
python generate_subsetfonts.py
```

---

## 開発者向け情報

### UnitCanvas レイアウト

-   **CSS**: `unitcanvas.css`
    -   `.unit` クラスがレイアウトの基本です。各要素の位置（`top`, `left`）やサイズ（`width`, `height`）は、CSSのIDセレクタ等で個別に指定します。
-   **HTML**: `index.html`
    -   レイアウトの構造を確認できます。

### Webフォントの仕組み

-   **フォント定義**: `fonts.css`
    -   `@font-face` でサブセットフォントを読み込み、`.f_フォント名` クラスで `font-family` を定義しています。
-   **サブセット生成スクリプト**: `generate_subsetfonts.py`
    -   HTMLを解析し、`f_` プレフィックスを持つクラスから使用されている文字を抽出し、`fonttools` ライブラリの `pyftsubset` を使ってサブセットフォントを生成します。
-   **元フォント**: `fonts/`
    -   サブセット化の元となる `.ttf` 形式のフォントを配置します。
-   **生成先**: `subfonts/`
    -   生成された `.woff` と `.woff2` ファイルが格納されます。

## ライセンス

MIT License
