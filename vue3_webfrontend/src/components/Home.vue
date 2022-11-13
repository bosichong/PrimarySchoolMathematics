<template lang="">
      <a-layout-content :style="{ margin: '24px 16px 0' }">
        <div :style="{ padding: '24px', background: '#fff', minHeight: '360px'}">
            
          <a-form layout="vertical">
            <a-space align="end">
              <a-form-item label="几步运算? ">
                <a-radio-group v-model:value="step" >
                    <a-radio-button value="1">一步运算</a-radio-button>
                    <a-radio-button value="2">两步运算</a-radio-button>
                    <a-radio-button value="3">三步运算</a-radio-button>
                </a-radio-group>
              </a-form-item>
              <a-form-item>
              <a-button type="primary" @click="showDrawer" >其他程序参数设置</a-button>
              </a-form-item>
            </a-space>

            <a-space align="end">
              <a-form-item label="算数项1">
                <a-input-group>
                  <a-row :gutter="8" >
                    <a-col :span="8">
                      <a-input v-model:value="multistep_a1" addon-before="最小值"/>
                    </a-col>
                    <a-col :span="8">
                      <a-input v-model:value="multistep_a2" addon-before="最大值"/>
                    </a-col>
                  </a-row>
                </a-input-group>
              </a-form-item>
            </a-space>

            <a-space align="end">
              <a-form-item label="第一步运算符号选择">
                <a-checkbox-group v-model:value="symbols_a" :options="plainOptions_a" />
              </a-form-item>
            </a-space>

            <a-space align="end">
              <a-form-item label="算数项2">
              <a-input-group>
                <a-row :gutter="8" >
                  <a-col :span="8">
                    <a-input v-model:value="multistep_b1" addon-before="最小值"/>
                  </a-col>
                  <a-col :span="8">
                    <a-input v-model:value="multistep_b2" addon-before="最大值"/>
                  </a-col>
                </a-row>
              </a-input-group>
            </a-form-item>
            </a-space>

            <a-space align="end" v-show="step==2 || step == 3">
              <a-form-item label="第二步运算符号选择">
                <a-checkbox-group v-model:value="symbols_b" :options="plainOptions_b" />
              </a-form-item>
            </a-space>

            <a-space align="end" v-show="step==2 || step ==3">
              <a-form-item label="算数项3">
              <a-input-group>
                <a-row :gutter="8" >
                  <a-col :span="8">
                    <a-input v-model:value="multistep_c1" addon-before="最小值"/>
                  </a-col>
                  <a-col :span="8">
                    <a-input v-model:value="multistep_c2" addon-before="最大值"/>
                  </a-col>
                </a-row>
              </a-input-group>
            </a-form-item>
            </a-space>

            <a-space align="end" v-show="step==3">
              <a-form-item label="第三步运算符号选择">
                <a-checkbox-group v-model:value="symbols_c" :options="plainOptions_c" />
              </a-form-item>
            </a-space>

            <a-space align="end" v-show="step==3">
              <a-form-item label="算数项4">
              <a-input-group>
                <a-row :gutter="8" >
                  <a-col :span="8">
                    <a-input v-model:value="multistep_d1" addon-before="最小值"/>
                  </a-col>
                  <a-col :span="8">
                    <a-input v-model:value="multistep_d2" addon-before="最大值"/>
                  </a-col>
                </a-row>
              </a-input-group>
            </a-form-item>
            </a-space>


            <a-space align="end">
              <a-form-item label="运算结果">
              <a-input-group>
                <a-row :gutter="8" >
                  <a-col :span="8">
                    <a-input v-model:value="multistep_e1" addon-before="最小值"/>
                  </a-col>
                  <a-col :span="8">
                    <a-input v-model:value="multistep_e2" addon-before="最大值"/>
                  </a-col>
                </a-row>
              </a-input-group>
            </a-form-item>
            </a-space>

            <a-space align="end">
              <a-form-item>
              <a-input-group>
                <a-row :gutter="20" >
                  <a-col :span="11">
                    <a-input v-model:value="number" addon-before="口算题数量"/>
                  </a-col>
                  <a-col :span="5">
                    <a-button type="primary" @click="handleCreatePSM" >添加口算题</a-button>
                  </a-col>
                  <a-col :span="5">
                    <a-button type="primary" @click="cleartext" >清空口算题</a-button>
                  </a-col>
                </a-row>
              </a-input-group>
            </a-form-item>
            </a-space>

            <a-space align="end">

              <a-input-group>
                  <a-row :gutter="99" >
                    <a-col :span="55">
                      <a-textarea v-model:value="psmtextarea" placeholder="当前口算题包含的内容" :rows="2" :cols="99" />
                    </a-col>
                      

                  </a-row>
                </a-input-group>
                
            </a-space>
            <a-button type="primary" @click="handleproducePSM" block >点此生成口算题卷子</a-button>

          </a-form>
        </div>
      </a-layout-content>

      <a-drawer title="其他程序参数设置" :width="550" :visible="visible" :body-style="{ paddingBottom: '80px' }"
    :footer-style="{ textAlign: 'right' }" @close="onClose">
      <a-space align="end">
              <a-form-item label="题型设置 ">
                <a-radio-group v-model:value="is_result" >
                    <a-radio-button value="0">求结果</a-radio-button>
                    <a-radio-button value="1">求算数项</a-radio-button>
                </a-radio-group>
              </a-form-item>

              <a-form-item label="启用括号() ">
                <a-switch v-model:checked="is_bracket" />
              </a-form-item>
            </a-space>

            <a-space align="end">
              <a-form-item label="加法设置 ">
                <a-radio-group v-model:value="carry" >
                    <a-radio-button value="1">随机进位</a-radio-button>
                    <a-radio-button value="2">加法进位</a-radio-button>
                    <a-radio-button value="3">没有进位</a-radio-button>
                </a-radio-group>
              </a-form-item>
            </a-space>

            <a-space align="end">
              <a-form-item label="减法设置 ">
                <a-radio-group v-model:value="abdication" >
                    <a-radio-button value="1">随机退位</a-radio-button>
                    <a-radio-button value="2">减法退位</a-radio-button>
                    <a-radio-button value="3">没有退位</a-radio-button>
                </a-radio-group>
              </a-form-item>
            </a-space>

            <a-space align="end">
              <a-form-item label="除法设置 ">
                <a-radio-group v-model:value="remainder" >
                    <a-radio-button value="1">随机余数</a-radio-button>
                    <a-radio-button value="2">结果整除</a-radio-button>
                    <a-radio-button value="3">结果余数</a-radio-button>
                </a-radio-group>
              </a-form-item>
            </a-space>

            <a-space align="end">
              <a-form-item>
              <a-input-group>
                <a-row :gutter="20" >
                  <a-col :span="9">
                    <a-input v-model:value="juanzishu" addon-before="生成的卷子数量"/>
                  </a-col>
                  <a-col :span="8">
                    <a-input v-model:value="lieshu" addon-before="口算题列数"/>
                  </a-col>
                </a-row>
              </a-input-group>
            </a-form-item>
            </a-space>

            <a-space align="end">
              <a-form-item>
              <a-input-group>
                <a-row :gutter="8" >
                  <a-col :span="33">
                    <a-input v-model:value="jz_title" addon-before="卷子标题"/>
                  </a-col>
                </a-row>
              </a-input-group>
            </a-form-item>
            </a-space>
            <a-input v-model:value="inf_title" addon-before="卷子副标题"/>

            
           


    </a-drawer>
</template>
<script setup>
import { ref, } from 'vue';
import { Modal } from 'ant-design-vue';
import axios from 'axios';


const psm_a = [] //最后需要生成的口算题参数数组,包含所有口算题的参数设置数组
const psm_b = {} // 其他口算卷子的剩余参数,一些固定的参数.
const baseURL = 'http://localhost:8000'



// 加载程序参数
console.log('少年，我看你骨骼精奇，是万中无一的编程奇才，有个程序员大佬qq群[217840699]你加下吧!维护世界和平就靠你了')

// 加载上次使用的配置项参数
axios.get(baseURL + '/api_getconfigjson').then(function (res) {
  let config = res.data.config
  // console.log(config)
  step.value = config.step.toString()
  is_result.value = config.is_result.toString()
  if (config.is_bracket > 0) {
    is_bracket.value = true
  } else {
    is_bracket.value = false
  }
  psmdocx.value = config.docx
  number.value = config.number
  juanzishu.value = config.juanzishu
  lieshu.value = config.lieshu
  jz_title.value = config.jz_title
  inf_title.value = config.inf_title

  carry.value = config.add.carry.toString()
  abdication.value = config.sub.abdication.toString()
  remainder.value = config.div.remainder.toString()

  multistep_a1.value = config.multistep[0][0]
  multistep_a2.value = config.multistep[0][1]
  multistep_b1.value = config.multistep[1][0]
  multistep_b2.value = config.multistep[1][1]
  multistep_c1.value = config.multistep[2][0]
  multistep_c2.value = config.multistep[2][1]
  multistep_d1.value = config.multistep[3][0]
  multistep_d2.value = config.multistep[3][1]
  multistep_e1.value = config.multistep[4][0]
  multistep_e2.value = config.multistep[4][1]

  symbols_a.value = getsymbols(config.symbols[0])
  symbols_b.value = getsymbols(config.symbols[1])
  symbols_c.value = getsymbols(config.symbols[2])

})

/**
 * 
 * @param {*} array 运算符号数组
 * @return  一组运算符号的ui配置数组
 */
const getsymbols = (array) => {
  let temparray = []
  for (let index = 0; index < array.length; index++) {
    const element = array[index];
    if (element === 1) {
      temparray.push('+(加法)')
    } else if (element === 2) {
      temparray.push('-(减法)')
    } else if (element === 3) {
      temparray.push('×(乘法)')
    } else if (element === 4) {
      temparray.push('÷(除法)')
    }
  }
  return temparray
}


// 几步运算
const step = ref('1')
// 题型设置
const is_result = ref('1')
// 启用括号
const is_bracket = ref(false)
// 加减乘除 设置
const carry = ref('1')
const abdication = ref('1')
const remainder = ref('2')
const psmdocx = ref('')
// 添加口算题的数量
const number = ref('30')
// 当前口算题包含的内容
const psmtextarea = ref('')

// 其他设置项
const lieshu = ref(3)
const juanzishu = ref(3)
const jz_title = ref('小学生口算题')
const inf_title = ref('姓名：__________ 日期：____月____日 时间：________ 对题：____道')

// 算数项取值
const multistep_a1 = ref(1)
const multistep_a2 = ref(9)
const multistep_b1 = ref(1)
const multistep_b2 = ref(9)
const multistep_c1 = ref(1)
const multistep_c2 = ref(9)
const multistep_d1 = ref(1)
const multistep_d2 = ref(9)
const multistep_e1 = ref(1)
const multistep_e2 = ref(9)





// 运算符号
const plainOptions_a = ['+(加法)', '-(减法)', '×(乘法)', '÷(除法)'];
const symbols_a = ref(['+(加法)',]) //默认选中

const plainOptions_b = ['+(加法)', '-(减法)', '×(乘法)', '÷(除法)'];
const symbols_b = ref(['+(加法)',]) //默认选中

const plainOptions_c = ['+(加法)', '-(减法)', '×(乘法)', '÷(除法)'];
const symbols_c = ref(['+(加法)',]) //默认选中

/**
 * 创建一组口算题的配置（为当前口算题添加内容）
 */
const handleCreatePSM = () => {
  let psm_tmp = {}
  psm_tmp.step = parseInt(step.value)
  psm_tmp.number = parseInt(number.value)
  psm_tmp.is_result = parseInt(is_result.value)
  if (is_bracket.value) {
    psm_tmp.is_bracket = 1
  } else {
    psm_tmp.is_bracket = 0
  }

  psm_tmp.add = {
    "carry": parseInt(carry.value)
  }
  psm_tmp.sub = {
    "abdication": parseInt(abdication.value)
  }
  psm_tmp.mult = {}
  psm_tmp.div = {
    "remainder": parseInt(remainder.value)
  }

  // 算数项
  psm_tmp.multistep = [
    [parseInt(multistep_a1.value), parseInt(multistep_a2.value),],
    [parseInt(multistep_b1.value), parseInt(multistep_b2.value),],
    [parseInt(multistep_c1.value), parseInt(multistep_c2.value),],
    [parseInt(multistep_d1.value), parseInt(multistep_d2.value),],
    [parseInt(multistep_e1.value), parseInt(multistep_e2.value),]
  ]

  // 算数符号
  let ss_a = []
  symadd(ss_a, symbols_a.value[0]); symadd(ss_a, symbols_a.value[1]); symadd(ss_a, symbols_a.value[2]); symadd(ss_a, symbols_a.value[3]);
  let ss_b = []
  symadd(ss_b, symbols_b.value[0]); symadd(ss_b, symbols_b.value[1]); symadd(ss_b, symbols_b.value[2]); symadd(ss_b, symbols_b.value[3]);
  let ss_c = []
  symadd(ss_c, symbols_c.value[0]); symadd(ss_c, symbols_c.value[1]); symadd(ss_c, symbols_c.value[2]); symadd(ss_c, symbols_c.value[3]);
  psm_tmp.symbols = [ss_a, ss_b, ss_c]


  // console.log(psm_tmp)
  axios.post(baseURL + '/api_createpsm', {
    data: psm_tmp
  },).then(function (res) {
    // console.log(res.data)
    if (res.data.info !== 0) {
      // console.log(res.data.info)
      let temptext = psmtextarea.value
      temptext += res.data.info
      psm_a.push(psm_tmp)
      psmtextarea.value = temptext

    } else {
      let modal = Modal.error()
      modal.update({
        title: '口算题配置错误!',
        content: '请仔细检查口算题的参数配置.',
      })
      modal.confirm()

    }
  }).catch(function (error) {
    // console.log(error.response)
  })
}

// 算数符号数组添加方法
const symadd = (arr, sym) => {
  if (sym === '+(加法)') {
    arr.push(1)
  } else if (sym === '-(减法)') {
    arr.push(2)
  } else if (sym === '×(乘法)') {
    arr.push(3)
  } else if (sym === '÷(除法)') {
    arr.push(4)
  }
}
// 清空口算题
const cleartext = () => {
  psmtextarea.value = ''
  psm_a.length = 0
}

/**
 * 生成口算题卷子并保存到/docx目录下
 */
const handleproducePSM = () => {
  // 生成口算题卷子并保存到/docx目录下
  //拼装剩余参数
  psm_b.juanzishu = parseInt(juanzishu.value)
  psm_b.lieshu = parseInt(lieshu.value)
  psm_b.docx = psmdocx.value
  psm_b.jz_title = jz_title.value
  psm_b.inf_title = inf_title.value
  const psm_data = [psm_a, psm_b]
  // console.log(psm_data)
  const psmjson_data = JSON.stringify(psm_data)
  axios.post(baseURL + '/api_producepsm', {
    data: psmjson_data
  },).then(function (res) {
    if (res.data.info) {
      let modal = Modal.info()
      modal.update({
        title: '提示!',
        content: res.data.info,
      })
      modal.confirm()
    }else{

    }

  }).catch(function(error){

  })

}



//  其他参数设置抽屉
const visible = ref(false);
const showDrawer = () => {
  visible.value = true;
};
const onClose = () => {
  visible.value = false;
};

</script>
<style lang="">
    
</style>