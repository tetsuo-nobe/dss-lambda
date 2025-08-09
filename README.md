# Developing Serverless Solutions on AWS における AWS Lambda ワーク


## 準備

* インストラクターが指定した環境で AWS マネジメントコンソールにサインインして下さい。
    - このワークの環境は、ワークを実施する時間帯のみ使用可能です。
    - ワークに関連する操作のみ実施して下さいますようお願い致します。
* AWS マネジメントコンソールで、リージョンを **バージニア北部 (us-east-1)**を選択した状態にしてください。
* ご自分に割り当てられた 2桁の番号を覚えておいてください。

---
## 1. AWS SAM を使用してワークで使用する Lambda 関数や API Gateway の REST API を作成

1. マネージメントコンソール上部で **CloudShell** のアイコンを選択します。
    - マネージメントコンソールの下部に CloudShell が表示されます。

1. CloudShell で下記のコマンドを実行し、AWS SAM プロジェクトを取得します。
    ```
    git clone https://github.com/tetsuo-nobe/dss-lambda
    ```

1. AWS SAM のプロジェクトフォルダに移動します。
    ```
    cd dss-lambda
    ```

1. AWS SAM のビルドを行います。
    ```
    sam build  --use-container
    ```

1. AWS SAM のデプロイを行います。
    ```
    sam deploy --guided
    ```
    - スタック名に `dss-lambda-<自分の番号>` を入力します。
    - Authorization の確認では `y` で応答します。
    - それ以外には、デフォルトのまま Enter キーを押下します。

1. デプロイ完了後に表示される **DemoAPI** の URL の値をメモしておきます。
    -  ブラウザでこの URL にアクセスして、背景色が青のページが表示されることを確認します。
---
## 2. Lambda 関数のバージョンとエイリアス 

1.


---
## 3. Lambda 関数の「予約された同時実行数」


---
## 4. Lambda 関数の Snapstart




---
## 3. 使用したリソースの削除


--
## お疲れさまでした。

* **このワークの環境は、ワークを実施する時間帯のみ使用可能です。**