# CloudBase 部署步骤

这份 Skill 要发布到 ClawHub，核心前提是先把 `mcp_server.py` 部署成一个公网可访问的 HTTP 服务。

## 推荐方案

推荐使用腾讯云 CloudBase 云托管，通过 GitHub 仓库部署。

原因：

- 当前项目已经补好 `Dockerfile`
- 云托管支持直接通过 Git 仓库部署
- 部署成功后会给你一个公网域名，后续可直接写入 `skill.json`

## 你需要准备的东西

1. 一个 GitHub 仓库
2. 一个腾讯云 CloudBase 环境
3. 这份项目代码推到 GitHub

## 第一步：推到 GitHub

先在 GitHub 网页创建一个空仓库，例如：

- 仓库名：`wangjucai-liangpi-skill`

然后在本地项目目录执行：

```bash
cd /Users/nian/Desktop/wangjucai-liangpi
git add .
git commit -m "Prepare Wangjucai Liangpi skill for publishing"
git remote add origin https://github.com/maggotnian-cell/wangjucai-liangpi-skill.git
git push -u origin main
```

## 第二步：在 CloudBase 创建云托管服务

1. 打开 CloudBase 控制台
2. 进入你的环境
3. 选择“云托管”
4. 选择“通过 Git 仓库部署”或“通过公开 Git 仓库地址部署”
5. 选择刚才的 GitHub 仓库和 `main` 分支

## 第三步：部署参数建议

- 服务端口：`8080`
- Dockerfile 路径：留空或填 `/`
- Dockerfile 文件名：`Dockerfile`
- 启动方式：使用 Dockerfile 默认命令
- 地域：按你的用户主要访问地区选择

## 第四步：拿到公网地址

部署完成后，CloudBase 会给你一个默认域名。

你需要确认下面这个地址可访问：

- `https://你的服务域名/`

正常情况下，访问后会返回类似：

```json
{
  "name": "wangjucai-liangpi",
  "version": "1.3.0",
  "status": "ok"
}
```

## 第五步：把真实地址写回 Skill

拿到真实公网地址后，把它写到：

- `skill.json` 的 `mcp_server.url`
- `README.md` 的 MCP 接入配置示例

如果你的服务直接挂在根路径 `/`，可以写成：

```json
{
  "mcp_server": {
    "transport": "streamable-http",
    "url": "https://your-real-domain.com/"
  }
}
```

## 第六步：再发布到 ClawHub

当 `mcp_server.url` 换成真实地址后，这个 Skill 才算真正可发布。

此时你再去 ClawHub 发布，别人安装后才能真正调用你的门店 AI 和公开下单入口。
