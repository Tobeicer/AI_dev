用户与agent对话描述不清，只能提出大概得需求，从模糊需求到完整落地，ai全栈开发工程师需要明确所有详细的实现方案和需求框架，因此从想法到落地需要在每一轮开发中进行详细的沟通和确认。因此需要让agent在每一轮开发中，都详细描述实现方案和需求框架，确保用户和agent对需求的理解一致，并参考现有的项目案例和最佳实践。  


AI开发入门:Agent、Skills、MCP、Langchain、Langgraph、dify  



Plugins:  
1.ponytail:精简代码，提高维护，优先采用现成方案，拒绝重读造轮子。(8.5)  
2.supervision:计算机视觉开发工具箱，从检测跟踪到可视化标注，一站式处理，无缝衔接YOLO。(8)  
3.Spec-kit:解决AI代码跑偏的问题，避免AI盲目编写，先定义需求，规则，实现思路，再编写代码。(8)  
4.humaizer-zh:中文重塑，修正翻译腔的字词组合。(8)  
5.Headroom:节省60-90%的Token，提取上下文重点，避免重复生成。(7.5)  
6.GitNexus:降低Token成本，提高开发效率。(6)  
7.Prompt Optimizer: 提示词优化工具，帮助用户生成更符合需求的提示词，提高模型的响应质量。(6)  
8.ECC AI:大模型强化工作流，给AI工具装一套专业的开发工作流(内置18个skill，47个代理，79个指令)。  
9.zvec:向量数据库，用于 RAG 存储和检索向量数据，如图片、文本等，支持向量检索和相似度计算。  
10.playwright:端到端浏览器自动化测试，用于测试和验证Web应用的交互和功能。(6)  


Skill:  
1.Superpowers:skill合集，包含brainstorming和test-driven-development等。(10)******  
2.brainstorming:引导式头脑风暴，将想法转化为设计文档和规格说明。(10)  
3.Planning with Files:把规划写进文件，上下文压缩了也不丢状态。(10)  
4.Code Review:多Agent并行审查代码，确保代码质量和一致性。(9)  
5.markitdown:把文档转换为markdown格式（基于微软开源项目自封装，非官方SKILL.md）。(9)  
6.ui-ux-pro-max:67种风格+161套配色，解决AI审美问题。(8.5)  
7.test-driven-development:测试驱动开发，先写测试再写代码，红-绿-重构循环。(8.5)  
8.MCP Builder:快速构建MCP服务器，低代码定义工具接口。(8.5)  
9.context engineering:上下文工程学，结构化压缩以最大化模型理解力。(8)  
10.also agent skills:Agent能力扩展包，增强自主规划与多步推理。(7.5)  
11.compose your skills:Skills编排组合工具，将多个Skill串联为完整工作流。(7.5)  
12.Code Simpliffer:代码精简与重构，消除冗余、提升可维护性。(7)  
13.Webapp Testing:Web应用自动化测试，端到端UI交互和兼容性检测。(7)  
14.PPTX:原生PowerPoint文件生成，支持图表、模板和多媒体。(7)  
15.antivo skills:对抗验证技能集，检测和修正AI输出的幻觉与偏差。(7)  
16.gsap-skills:官方级动画代码，时间轴控制，滚动动画，路径动画，ScrollTrigger等各种复杂动画生成，用于交互式网页开发。(6)  
17.supercloud framework:多云统一部署框架，简化跨平台运维。(6)  
18.minimax cues:MiniMax提示词模板库，优化多模态生成效果。(6)  
19.impeccable:前端skill，提升前端页面质量和高级质感。(5)  
20.taste-skill:前端skill。提升前端设计品味。(5)  
21.amsp-skills:高德地图skill，提升地图功能和交互体验(含API)。(3)  




Codex插件:  
1.Computer Use: 操作本机App，如打开文件、发送邮件、打开浏览器等。(10)  
2.GitHub: 操作GitHub仓库，如克隆仓库、提交代码、创建Pull Request等。(10)  
3.Superpowers:把顶级工程能力拆成技能点，避免初步就盲目编写，先通过提问整理需求并梳理思路，给出分步实施方案。(10)  
4.Presentations: 写PPT。(9)  
5.Documents: 正式文档交付。(9)  
6.Chrome:控制谷歌浏览器。(9)  
7.Browser: 网页调试插件，支持在浏览器中调试代码，查看DOM元素、网络请求等。(8.5)  
8.Remotion: 程序化视频，支持从图片序列创建视频。(8)  
9.Canva:图形设计、海报制作、社交媒体素材生成。(8)  
10.HyperFrames by HeyGen:自然语言打造动态页面效果。(7)  
11.Build Web Apps: 快速开发网页。  
12.Figma: 需求或代码转成figma设计稿，也能创建图表和设计系统。  
13.Vercel: 部署网页到Vercel，支持自动部署和监控。  
14.Spreadsheets: 能生成带公式、格式、图表和分析结果的表格。  
15.Windsor.ai:用于进行营销数据分析。  
16.BioRender:创建专业的科学插图和图标。  


MCP:  
1.brave-search-mcp-server:联网搜索，需要先有一个它的API key，每月2000次免费。  
安装指令:claude mcp add brave-search -e BRAVE_SEARCH_API_KEY=****** --npx -y @brave/brave-search-mcp-server
2.fetch:网页读取。  
安装指令:claude mcp add fetch --npx -y @modelcontextprotocol/server-fetch
3.Screenshot MCP:图片识别。  
安装指令:claude mcp add screenshot --npx -y mcp-screenshot-server


组件库:  
1.Ant Design，前端react组件库，提供丰富的组件和样式。  
2.https://lucide.dev/:提供丰富的图标组件。  




框架：  
1.Langchain：LLM应用开发框架，链式调用、Agent、RAG、记忆组件。  
2.Langgraph：有状态Agent工作流引擎，支持条件分支、循环和多Agent。  
3.Bernini：字节开源的视频生成框架。  


