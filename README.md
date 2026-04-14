# 王聚财面皮铺 AI Skill

> 西安首家芥末蒜香酿皮，擀面皮人气榜 TOP。一个已经完成公开发布的餐饮门店 AI Skill。

## 快速入口

- ClawHub：<https://clawhub.ai/maggotnian-cell/wangjucai-liangpi>
- GitHub：<https://github.com/maggotnian-cell/wangjucai-liangpi-skill>
- MCP 服务：<https://wangjucai-liangpi-246135-8-1421953131.sh.run.tcloudbase.com>
- 公开下单入口：<https://rms.meituan.com/diancan/14/2HpfZPxOFw0>

## 这是什么

这是一个面向餐饮门店的 MCP Skill，目标是让 AI 帮用户完成“了解门店、查看菜单、判断能不能点、拿到下单入口”这一整套流程。

当前已经支持：

- 查询店铺地址、电话、营业时间、人均消费
- 查询菜单、特色菜、价格与推荐吃法
- 查询外卖与堂食预约信息
- 提供到店 Wi-Fi 获取指引
- 直接返回公开下单链接，并提示用户到店也可扫码进入同一入口

## 适合谁用

- 想把门店接入 AI 的餐饮商家
- 想给用户一个可公开访问的门店智能入口
- 想研究本地生活场景 Skill 的开发者
- 想直接体验“AI 帮忙接待和引导点单”的朋友

## 店铺信息

| 项目 | 内容 |
|------|------|
| 店名 | 王聚财面皮铺 |
| 地址 | 西安市凤城6路ee新城南门底商 |
| 商圈 | 张家堡商圈，西安北站附近 |
| 电话 | 19537080416 |
| 营业时间 | 9:00 - 21:00 |
| 人均 | 12-13元 |
| 评分 | 大众点评4.6-4.7分 |

## 特色菜品

- **芥末蒜香酿皮**（8元）：招牌特色，西安首家
- **经典擀面皮**（8元）：劲道有嚼劲，辣椒香而不辣
- **辣肠夹馍**（9元）：经典搭配

## Skill 能力

| 工具 | 功能 |
|------|------|
| `get_restaurant_info` | 餐厅基本信息 |
| `get_menu` | 菜单与特色菜介绍 |
| `get_delivery_info` | 外卖配送信息 |
| `get_reservation_info` | 堂食预约信息 |
| `get_wifi_info` | 到店 Wi-Fi 指引，公开版不返回密码 |
| `get_order_entry` | 公开下单入口，AI 可直接提供链接，也可提示到店扫码 |

## 公开发布安全说明

- 不公开店内 Wi-Fi 密码
- 不公开门店扫码点单二维码图片
- 保留二维码对应的公开下单链接，方便 AI 与用户直接使用
- 本地调试默认仅监听 `127.0.0.1`
- MCP 返回按 JSON-RPC 封装，便于接入平台

## 安装方式

### 方式一：告诉 AI 助手

```text
帮我安装王聚财面皮铺 Skill，仓库地址：https://github.com/maggotnian-cell/wangjucai-liangpi-skill
```

### 方式二：手动克隆

```bash
git clone https://github.com/maggotnian-cell/wangjucai-liangpi-skill.git \
  ~/.hermes/skills/mcp/wangjucai-liangpi
```

## MCP 接入配置

```json
{
  "mcpServers": {
    "wangjucai-liangpi": {
      "type": "streamable-http",
      "url": "https://wangjucai-liangpi-246135-8-1421953131.sh.run.tcloudbase.com"
    }
  }
}
```

## 本地运行

```bash
cd ~/.hermes/skills/mcp/wangjucai-liangpi
python mcp_server.py
```

默认监听 `127.0.0.1:8080`。然后访问：

- `GET http://127.0.0.1:8080/`：健康检查
- `POST http://127.0.0.1:8080/`：MCP 协议调用

获取公开下单入口示例：

```bash
curl -X POST http://127.0.0.1:8080/ \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":2,"method":"tools/call","params":{"name":"get_order_entry"}}'
```

如需对外监听，请显式设置：

```bash
MCP_HOST=0.0.0.0 python mcp_server.py
```

## CloudBase 部署

项目已经包含 `Dockerfile`，推荐直接走 GitHub 仓库部署路线。

详细步骤请看 [DEPLOY_CLOUDBASE.md](./DEPLOY_CLOUDBASE.md)。

## 对外分享

对普通用户，优先分享 ClawHub 页面：

- <https://clawhub.ai/maggotnian-cell/wangjucai-liangpi>

对开发者或合作方，可同时提供：

- GitHub 仓库：<https://github.com/maggotnian-cell/wangjucai-liangpi-skill>
- MCP 地址：<https://wangjucai-liangpi-246135-8-1421953131.sh.run.tcloudbase.com>

具体分享文案可直接看 [SHARE_COPY.md](./SHARE_COPY.md)。

## 发布记录

- 当前版本：`1.3.0`
- 发布说明见：[RELEASE_NOTES.md](./RELEASE_NOTES.md)
- 发布前检查清单见：[PUBLISHING.md](./PUBLISHING.md)

## 项目结构

```text
wangjucai-liangpi/
├── .gitignore          # Git 忽略规则
├── .dockerignore       # Docker 构建忽略规则
├── Dockerfile          # CloudBase 云托管部署文件
├── DEPLOY_CLOUDBASE.md # CloudBase 部署说明
├── LICENSE             # MIT 许可证
├── PUBLISHING.md       # 发布前检查清单
├── README.md           # 项目主页说明
├── RELEASE_NOTES.md    # 发布说明
├── SHARE_COPY.md       # 对外分享文案
├── SKILL.md            # Agent 指令文档
├── skill.json          # 机器可读配置
├── mcp_server.py       # MCP 服务器实现
└── tests/              # 基础兼容性测试
```

## 关联项目

**西安AI搞钱联盟**：以王聚财面皮铺为据点，打造西安 AI 创业者线下聚会与线上组织。

## License

MIT
