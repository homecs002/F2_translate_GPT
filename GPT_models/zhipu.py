from zhipuai import ZhipuAI

import os
import sys
sys.path.append("..")
sys.path.append(".")  #!

if os.path.exists("config_private.py"):
    import config_private as con
else:
    import config as con

api_key = con.Zhipu_API
model = con.Zhipu_model_name


def call_zhipu_api(input_text) -> str:
    client = ZhipuAI(api_key=api_key) 
    response = client.chat.completions.create(
        model= model, 
        messages=[
            {"role": "user", "content": "你是经验丰富的翻译，请把以下计算机科学和人工智能领域的学术文章段落翻译成中文，并同时充分考虑中文的语法、清晰、简洁和整体可读性，必要时，你可以修改整个句子的顺序以确保翻译后的段落符合中文的语言习惯，并且保留专业词汇的英文版本。注意，如果文本里有agent，请翻译成“智能体”。特别的，如果文本只有一个单词，则只需要翻译这个单词并给出音标即可，你需要翻译的文本如下：" + input_text},
        ],
    )
    return response.choices[0].message.content

# print(call_zhipu_api("Design Principles. Based on the key ingredients of prompts, we summarize several critical design principles that can help create more effective prompts for solving various tasks."))