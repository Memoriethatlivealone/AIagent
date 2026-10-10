def get_model_from_init():
    import os
    import dotenv
    from langchain.chat_models import init_chat_model

    # 1. 加载环境变量
    dotenv.load_dotenv()

    # 2. 初始化模型
    llm = init_chat_model(
        model="gpt-5.6-sol",
        model_provider="openai",
        base_url=os.getenv("OPENAI_BASE_URL"),
        api_key=os.getenv("OPENAI_API_KEY"),
    )

    # 3. 调用模型
    resp = llm.invoke("你是什么模型")

    # 4. 查看返回对象类型
    print(type(resp))

    # 5. 获取模型回答
    print(resp.content)


# get_model_from_init()


# 提示词
def prompt_template_demo():
    import dotenv
    from langchain.chat_models import init_chat_model
    from langchain_core.prompts import ChatPromptTemplate

    # 1. 加载环境变量
    dotenv.load_dotenv()

    # 2. 创建提示词模板
    chat_prompt_template = ChatPromptTemplate.from_messages(
        [
            ("system", "你是一个专业的评论员"),
            ("human", "请评价{product}，包括{aspect1}和{aspect2}。"),
        ]
    )

    # 3. 填充模板变量
    chat_message_list = chat_prompt_template.invoke(
        {
            "product": "macbook air m5 16g+512g",
            "aspect1": "价格",
            "aspect2": "是否适合购买和购买性价比",
        }
    )

    # 4. 初始化大模型
    llm = init_chat_model(
        model="gpt-5.6-sol",
        model_provider="openai",
    )

    # 5. 调用模型
    resp = llm.invoke(chat_message_list)

    # 6. 输出结果
    print(resp.content)


prompt_template_demo()
