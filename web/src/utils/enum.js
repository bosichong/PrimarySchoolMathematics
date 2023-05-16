/**
 * 文件名生成规则
 */
export const fileNameGeneratedRuleEnum = {
  baseOnTitleAndIndex: { key: 'baseOnTitleAndIndex', text: '卷子标题+时间' },
  baseOnIndexOnly: { key: 'baseOnIndexOnly', text: '仅时间' }
}

/**
 * response的content type与文件扩展名mapping关系
 */
export const httpContentTypeExtensionsMappingEnum = {
  'application/zip': 'zip'
}