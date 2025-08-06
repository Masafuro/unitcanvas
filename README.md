# unitcanvas
A lightweight layout system for HTML that enables precise, canvas-like positioning of DOM elements using structured data. UnitCanvas separates structure from presentation for highly maintainable, programmatically generated interfaces.

UnitCanvas は、HTML要素をキャンバスのように自由に配置するための軽量レイアウト手法です。
各要素（divなど）は HTML で構造として記述し、座標やサイズ、装飾は CSS で管理します。従来のグリッドやフローに依存せず、ピクセル単位で正確なUIレイアウトが可能です。

## 特徴

- top, left, width, height を使った絶対座標指定
- .unit クラスによる共通レイアウトスタイル
- HTMLには構造のみ、CSSに見た目と位置を分離
- レスポンシブ対応もメディアクエリで明快に制御
- DOMベースのため、コピー・SEO・アクセシビリティにも対応

### サンプル表示
<img width="1155" height="584" alt="スクリーンショット 2025-08-07 081721" src="https://github.com/user-attachments/assets/944d3bcf-0536-48f5-876c-799964c31173" />
<img width="471" height="550" alt="スクリーンショット 2025-08-07 081653" src="https://github.com/user-attachments/assets/efea1a36-75d3-4779-adea-790dac1e60a3" />



## 基本構成

HTML: 要素を定義
```html
<div class="canvas">
  <div id="box1" class="unit">ハローA</div>
  <div id="box2" class="unit">ハローB</div>
</div>
```
CSS: 共通スタイルと位置・サイズ指定
```css
.canvas {
  position: relative;
  width: 800px;
  height: 600px;
  margin: 20px auto 0;
}

.unit {
  position: absolute;
  overflow: hidden;
  padding: 0;
  margin: 0;
  box-sizing: border-box;
}

#box1 {
  top: 100px;
  left: 120px;
  width: 200px;
  height: 80px;
}

#box2 {
  top: 220px;
  left: 300px;
  width: 250px;
  height: 100px;
}
```
## レイアウト指針

- すべての要素は .canvas の中に配置します
- それぞれの要素には .unit を付与します
- 座標・サイズは id セレクタで個別にCSS定義します
- フォントや装飾も基本的にCSSで制御します

## 活用例

- 帳票・ラベル・名刺などの定型レイアウト
- UIモック・プロトタイプの描画
- テキストや画像を重ねた静的構成の設計
- 自動レイアウトツールとの連携基盤

## ライセンス
------

MIT License
