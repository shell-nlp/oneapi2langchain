from langchain.chat_models.baidu_qianfan_endpoint import QianfanChatEndpoint

if __name__ == "__main__":
    from dotenv import load_dotenv

    load_dotenv()
    llm = QianfanChatEndpoint()
    ret = llm.predict("你是谁")
    print(ret)
