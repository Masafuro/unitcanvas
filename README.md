# UnitCanvas & Webfont Tools

HTML要素をキャンバスのように自由に配置する `UnitCanvas` レイアウトシステムと、日本語フォントを最適化するサブセット化ツールのプロジェクトです。

## 概要

このプロジェクトは、主に2つの機能を提供します。

1.  **UnitCanvas**: CSSの絶対座標を使って、HTML要素をピクセル単位で正確に配置する軽量なレイアウト手法です。
2.  **Webフォント最適化**: HTMLで実際に使用されている文字だけを抽出した、軽量なWebフォント（サブセットフォント）を自動生成します。

デザイナーやコンテンツ編集者は、HTMLとCSS、簡単なコマンド操作で、デザインの制作や調整が可能です。

### 利用サンプル
<img width="1155" height="584" alt="スクリーンショット 2025-08-07 081721" src="https://github.com/user-attachments/assets/944d3bcf-0536-48f5-876c-799964c31173" />
<img width="471" height="550" alt="スクリーンショット 2025-08-07 081653" src="https://github.com/user-attachments/assets/efea1a36-75d3-4779-adea-790dac1e60a3" />

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

## デザインの調整方法（デザイナー向け）

デザインの調整は、主に「HTMLで要素を追加・編集」し、「CSSで見た目を定義」する2つのステップで行います。

### 1. HTMLで要素を配置する

まず、`index.html` にレイアウトしたい要素（テキスト、画像など）を追加します。各要素は `div` タグで囲み、以下の2つの属性を必ず指定してください。

-   `class="unit"`: すべてのレイアウト要素に共通でつけるクラスです。
-   `id="unique-name"`: CSSから個別にスタイルを指定するための、ユニークな（他と重複しない）名前をつけます。

**例: `index.html` の中身**
```html
<body>
  <div class="canvas-pc">
    <!-- ↓ここからが要素の例 -->
    <div id="title-text" class="unit">これはタイトルです</div>
    <div id="body-text" class="unit">これは本文です。</div>
    <div id="logo-image" class="unit"><img src="path/to/image.png" alt="logo"></div>
    <!-- ↑ここまで -->
  </div>
</body>
```

### 2. CSSでスタイルを調整する

次に、`unitcanvas.css` を編集して、HTMLで追加した要素の見た目を調整します。`id` 名を使って、位置、サイズ、色などを指定します。

**例: `unitcanvas.css` の中身**
```css
#title-text {
  top: 50px;
  left: 100px;
  width: 300px;
  height: 40px;
  font-size: 24px;
}

#body-text {
  top: 100px;
  left: 100px;
  width: 500px;
  height: 150px;
}
```
このように、HTMLで構造を作り、CSSで見た目を細かく調整していくのが基本的な流れです。

---

## 開発者向け情報

### UnitCanvas レイアウト

-   **CSS**: `unitcanvas.css`
    -   `.unit` クラスがレイアウトの基本です。各要素の位置・サイズはIDセレクタで個別に指定します。
-   **HTML**: `index.html`
    -   レイアウトの構造を確認できます。

### Webフォントの仕組み

-   **フォント定義**: `fonts.css`
    -   `@font-face` でサブセットフォントを読み込み、`.f_フォント名` クラスで `font-family` を定義しています。
-   **サブセット生成スクリプト**: `generate_subsetfonts.py`
    -   HTMLを解析し、`f_` プレフィックスを持つクラスから使用されている文字を抽出し、`fonttools` を使ってサブセットフォントを生成します。
-   **元フォント**: `fonts/`
    -   サブセット化の元となる `.ttf` 形式のフォントを配置します。
-   **生成先**: `subfonts/`
    -   生成された `.woff` と `.woff2` ファイルが格納されます。

## ライセンス

MIT License
