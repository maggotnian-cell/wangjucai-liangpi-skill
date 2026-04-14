# 王聚财面皮铺 Skill 发布说明

## v1.3.0

发布日期：2026-04-14

### 发布入口

- ClawHub：<https://clawhub.ai/maggotnian-cell/wangjucai-liangpi>
- GitHub：<https://github.com/maggotnian-cell/wangjucai-liangpi-skill>
- MCP 服务：<https://wangjucai-liangpi-246135-8-1421953131.sh.run.tcloudbase.com>
- 公开下单入口：<https://rms.meituan.com/diancan/14/2HpfZPxOFw0>

### 本版重点

- 完成 ClawHub 正式发布，可供外部用户直接查看和安装
- 完成 GitHub 公开仓库发布，便于开发者查看实现和二次接入
- 完成 CloudBase 公网部署，MCP 服务可被外部平台调用
- 将原二维码能力升级为公开下单链接，AI 可直接提供下单入口

### 功能范围

- 查询店铺基础信息：地址、营业时间、电话、人均
- 查询菜单与特色菜介绍
- 查询外卖配送和堂食预约信息
- 提供到店 Wi-Fi 获取指引
- 提供公开下单入口，并提醒用户到店也可扫码进入同一入口

### 安全处理

- 不公开店内 Wi-Fi 密码
- 不公开门店扫码点单二维码图片
- 保留二维码对应的公开下单链接，方便 AI 与用户直接使用
- MCP 响应按 JSON-RPC 方式封装，兼容平台接入

### 适合分享给谁

- 想通过 AI 了解店铺信息的普通用户
- 想把门店接入 AI 的商家朋友
- 需要二次接入 MCP 的开发者或平台方

