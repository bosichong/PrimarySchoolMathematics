import { fileNameGeneratedRuleEnum } from "./enum"

const key = 'customer-config'

export function loadConfiguration() {
  const stringValue = localStorage.getItem(key)
  if (stringValue) {
    return JSON.parse(stringValue)
  } else {
    // todo 初始化配置
    return {
      step: '1', // 几步运算
      numberOfFormulas: 30, // 口算题数量
      whereIsResult: '0', // 题型设置
      enableBrackets: false, // 启用括号
      carry: '1',
      abdication: '1',
      remainder: '2',
      solution: '0', // 解题方式
      numberOfPapers: 3, // 试卷数量
      numberOfPagerColumns: 3, // 试卷列数
      paperTitle: '小学生口算题', // 试卷标题
      paperSubTitle: '姓名：__________ 日期：____月____日 时间：________ 对题：____道', // 试卷副标题
      // 试题格式
      // min 算数项最小值 max 算数项最大值 operators 与上一步算数项使用的运算符号
      // 第一个算数项由于没有上一步故设置为null
      formulaList: [
        { min: 1, max: 9, operators: null },
        { min: 1, max: 9, operators: [1] },
      ],
      resultMinValue: 1, // 试题运行结果最小值
      resultMaxValue: 9, // 试题运行结果最大值
      fileNameGeneratedRule: fileNameGeneratedRuleEnum.baseOnTitleAndIndex.key
    }
  }
}

export function saveConfiguration(data) {
  const stringValue = JSON.stringify(data)
  return localStorage.setItem(key, stringValue)
}

export function removeConfiguration() {
  return localStorage.removeItem(key)
}
