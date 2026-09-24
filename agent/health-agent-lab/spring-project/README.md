# spring-project · Spring Boot Hello World

> 学习计划 S0 收尾任务：搭建第一个 Spring Boot 项目，跑通 `GET /api/health` 接口。

## 技术栈

| 项 | 版本 |
|---|---|
| JDK | 17 |
| Spring Boot | 3.5.16（3.5.x 最新） |
| Maven | 3.9.x |
| 构建插件 | spring-boot-maven-plugin |

## 项目结构

```
spring-project/
├── pom.xml                                      # 项目描述：依赖 + 构建配置
└── src/
    ├── main/
    │   ├── java/com/healthagent/
    │   │   ├── SpringProjectApplication.java    # 启动入口（main 方法）
    │   │   └── controller/
    │   │       └── HealthController.java        # GET /api/health 接口
    │   └── resources/
    │       └── application.yml                  # 配置：应用名、端口
    └── test/java/com/healthagent/
        ├── SpringProjectApplicationTests.java   # 上下文加载测试
        └── controller/
            └── HealthControllerTest.java        # 接口测试（MockMvc）
```

## 本地运行（三步跑通）

### ⓪ 前置检查（首次）

```powershell
java -version    # 应为 17.x
mvn -v           # 应输出 Maven 版本 + Java 17
```

### ① 进入项目目录

```powershell
cd agent\health-agent-lab\spring-project
```

### ② 启动服务

```powershell
mvn spring-boot:run
```

看到日志 `Started SpringProjectApplication in x.xxx seconds` 即启动成功（默认端口 8080）。

> 也可以用 IDEA：打开项目 → 运行 `SpringProjectApplication` 类。

### ③ 调用接口（另开一个终端，不要关掉服务）

```powershell
curl.exe http://localhost:8080/api/health
```

预期返回：

```json
{"status":"ok","service":"spring-project","time":"2026-09-24 14:30:00"}
```

PowerShell 原生写法（等价）：

```powershell
Invoke-RestMethod http://localhost:8080/api/health
```

## 跑测试（可选）

```powershell
mvn test
```

包含：上下文加载测试 + `/api/health` 接口测试（MockMvc，无需启动服务器）。

## 常见问题

| 问题 | 处理 |
|---|---|
| 端口 8080 被占用 | 修改 `application.yml` 的 `server.port`（如 8081），接口地址同步变化 |
| 首次启动很慢 | 正常：第一次在下载依赖；配好阿里云镜像后会快很多 |
| `mvn` 命令找不到 | 检查 `MAVEN_HOME` 与 `PATH`（见 d1.md 的 Maven 笔记） |
| 怎么停止服务 | 回到启动服务的终端按 `Ctrl + C` |
| 想换 Spring Boot 版本 | 改 `pom.xml` 里 parent 的 `version`（本计划统一 3.5.x，与教程 / 资料更一致） |
