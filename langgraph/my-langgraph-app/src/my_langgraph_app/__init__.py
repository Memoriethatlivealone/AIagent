from typing import TypedDict
def main() -> None:
    print("Hello from my-langgraph-app!")


# 1 定义状态
class MyAgentState(TypedDict):
    query: str
    rag_search: str = ""
    web_search: str = ""
    llm_answer: str = ""
# 2 定义节点
def rag_node(state: MyAgentState) -> MyAgentState:
    #1从state中获取query
    query = state["query"]
    #2模拟rag检索
    rag_serch=f"根据用户的问题{query}，在知识库中检索到的相关内容"

    return {"rag_search": rag_serch}
    # 这里是RAG节点的逻辑

def web_search_node(state: MyAgentState) -> MyAgentState:
    #1从state中获取query
    query = state["query"]
    #2模拟web检索
    web_serch=f"根据用户的问题{query}，在网络中检索到的相关内容"
    return {"web_search": web_serch}
    # 这里是Web搜索节点的逻辑
    
# 3 构建builder

#4 编译图

#5 调用图
