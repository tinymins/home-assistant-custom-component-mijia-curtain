# 米家平台窗帘 home assistant 插件

> Mijia Curtain 是一款ha自定义插件, 通过miot协议接入到homeassistant
>
> 支持开合帘、设置开合位置、状态监控等功能

## 支持型号，米家平台所有开启MIoT协议的窗帘

## 安装方式

1. **推荐：** 使用 HACS 安装

    * 打开 HACS 自定义仓库。
    * 输入 https://github.com/tinymins/home-assistant-custom-component-mijia-curtain 点击确定。
    * 找到刚刚添加的自定义插件，点击下载安装。

2. 不推荐： 手动下载

    * 下载下面网址所有文件到如下目录/config/custom_components/
    * https://github.com/tinymins/home-assistant-custom-component-mijia-curtain/tree/main/custom_components

    ```shell
    //文件目录结构如下
    /config/custom_components/mijia_curtain/__init__.py
    /config/custom_components/mijia_curtain/config_flow.py
    /config/custom_components/mijia_curtain/const.py
    /config/custom_components/mijia_curtain/cover.py
    /config/custom_components/mijia_curtain/manifest.json
    ```

## 配置方式

1. 在 Home Assistant 的集成页面中点击"添加集成"
2. 搜索"Mijia Curtain"
3. 填写以下信息：
   - 名称：设备在 HA 中显示的名称
   - 主机：窗帘电机 IP 地址（需要在路由器设为固定 IP）
   - Token：米家设备 token
   - 型号：设备型号（可选，如果未填写会自动从网络获取）
   - 刷新间隔：状态刷新间隔（秒），默认 30

## 米家token获取

```url
https://github.com/tiandeyu/Xiaomi-cloud-tokens-extractor
```

### 已验证型号 model

> 如果ha环境没有外网可以手工填写model配置，仅支持以下几个型号
> 未验证型号直接填写token，会自动从网络拉取model配置
> C1为卷帘控制器，支持香格里拉帘角度控制

| 名称 | 型号 |
| :---- | :--- |
| 杜亚M1 | dooya.curtain.m1 |
| 杜亚M2 | dooya.curtain.m2 |
| 杜亚卷帘控制器C1 | dooya.curtain.c1 |
| 情景开合电机WIFI X版（闲鱼米家电机） | babai.curtain.bb82mj |
| 绿米窗帘电机WIFI版 | lumi.curtain.hagl05 |
| 绿米窗帘电机WIFI版 | lumi.curtain.hmcn01 |

### 不支持型号

| 名称 | 型号 |
| :---- | :--- |
| 邦先生智能晾衣机-简约款 | mrbond.airer.m1tpro |
