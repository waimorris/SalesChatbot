import gradio as gr

from langchain_mistralai import MistralAIEmbeddings
from langchain.chains import RetrievalQA
from langchain_mistralai import ChatMistralAI

from langchain_community.vectorstores import FAISS


def initialize_sales_bot(vector_store_dir: str="real_machine_sale"):
    db = FAISS.load_local(vector_store_dir, MistralAIEmbeddings(api_key="rDjmdXGVUS37qMW2NOFP5vCpqlpve6Yt"),allow_dangerous_deserialization=True)
    llm = llm = ChatMistralAI(
    model="mistral-large-latest",
    temperature=0,
    max_retries=2,
    api_key= "rDjmdXGVUS37qMW2NOFP5vCpqlpve6Yt"
)
    
    global SALES_BOT    
    SALES_BOT = RetrievalQA.from_chain_type(llm,
                                           retriever=db.as_retriever(search_type="similarity_score_threshold",
                                                                     search_kwargs={"score_threshold": 0.8}))
    # 返回向量数据库的检索结果
    SALES_BOT.return_source_documents = True

    return SALES_BOT

def sales_chat(message, history):
    print(f"[message]{message}")
    print(f"[history]{history}")
    # TODO: 从命令行参数中获取
    enable_chat = True

    ans = SALES_BOT({"query": message})
    # 如果检索出结果，或者开了大模型聊天模式
    # 返回 RetrievalQA combine_documents_chain 整合的结果
    if ans["source_documents"] or enable_chat:
        print(f"[result]{ans['result']}")
        print(f"[source_documents]{ans['source_documents']}")
        return ans["result"]
    # 否则输出套路话术
    else:
        return "这个问题我要问问领导"
    

def launch_gradio():
    demo = gr.ChatInterface(
        fn=sales_chat,
        title="家電销售",
        # retry_btn=None,
        # undo_btn=None,
        chatbot=gr.Chatbot(height=600),
    )

    demo.launch(share=True, server_name="0.0.0.0")

if __name__ == "__main__":
    initialize_sales_bot()
    # 启动 Gradio 服务
    launch_gradio()
