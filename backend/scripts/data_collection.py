import json
import os
from typing import List, Dict


def create_sample_legal_data():
    """
    创建示例法律训练数据
    后续需要替换为真实的法律条文和案例
    """
    sample_data = [
        {
            "instruction": "回答关于劳动合同的问题",
            "input": "试用期最长可以约定多久？",
            "output": "根据《劳动合同法》第十九条：劳动合同期限三个月以上不满一年的，试用期不得超过一个月；劳动合同期限一年以上不满三年的，试用期不得超过二个月；三年以上固定期限和无固定期限的劳动合同，试用期不得超过六个月。"
        },
        {
            "instruction": "回答关于劳动报酬的问题",
            "input": "加班工资怎么计算？",
            "output": "根据《劳动法》第四十四条：工作日加班支付不低于工资的150%的工资报酬；休息日加班又不能安排补休的支付不低于工资的200%的工资报酬；法定休假日加班支付不低于工资的300%的工资报酬。"
        },
        {
            "instruction": "回答关于劳动合同解除的问题",
            "input": "什么情况下用人单位可以单方面解除劳动合同？",
            "output": "根据《劳动合同法》第三十九条，劳动者有下列情形之一的，用人单位可以解除劳动合同：（一）在试用期间被证明不符合录用条件的；（二）严重违反用人单位的规章制度的；（三）严重失职，营私舞弊，给用人单位造成重大损害的；（四）劳动者同时与其他用人单位建立劳动关系，对完成本单位的工作任务造成严重影响，或者经用人单位提出，拒不改正的；（五）因本法第二十六条第一款第一项规定的情形致使劳动合同无效的；（六）被依法追究刑事责任的。"
        }
    ]

    # 确保数据目录存在
    os.makedirs("../data/processed", exist_ok=True)

    # 保存为JSON文件
    with open("../data/processed/legal_training_data.json", "w", encoding="utf-8") as f:
        json.dump(sample_data, f, ensure_ascii=False, indent=2)

    print(f"已创建示例数据，共 {len(sample_data)} 条记录")
    print("文件保存在: ../data/processed/legal_training_data.json")


if __name__ == "__main__":
    create_sample_legal_data()