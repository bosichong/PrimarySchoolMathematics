import { fileNameGeneratedRuleEnum } from "./enum"


export default class {
  key = 'customer-config'

  constructor() {

  }

  #getConfigurations() {
    const stringValue = localStorage.getItem(this.key)
    return stringValue && JSON.parse(stringValue)
  }

  #setConfigurations(configurations) {
    localStorage.setItem(this.key, JSON.stringify(configurations))
  }

  load() { }

  loadAll() {
    const configurations = this.#getConfigurations()
    if (configurations) {
      return configurations
    } else {
      const initConfiguration = [{
        id: '1',
        name: '默认',
        data: {
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
      }]
      this.#setConfigurations(initConfiguration)
      return initConfiguration
    }
  }

  save(id, name, configuration) {
    const configurations = this.#getConfigurations()
    configurations.push({ id, name, data: configuration })
    this.#setConfigurations(configurations)
  }

  remove(id) {
    const configurations = this.#getConfigurations()
    const index = configurations.findIndex(p => p.id == id)
    configurations.splice(index, 1)
    this.#setConfigurations(configurations)
  }

  clear() {
    localStorage.removeItem(this.key)
  }
} 