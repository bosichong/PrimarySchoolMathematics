import img_01 from '../img_01.jpeg'
import React from 'react';
import axios from 'axios';
import { useState, useEffect } from 'react';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';


import Box from '@mui/material/Box';

import Grid from '@mui/material/Grid';

import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';

import FormGroup from '@mui/material/FormGroup';
import FormControlLabel from '@mui/material/FormControlLabel';
import Switch from '@mui/material/Switch';
import TextField from '@mui/material/TextField';
import Checkbox from '@mui/material/Checkbox';
import FormLabel from '@mui/material/FormLabel';

import Link from '@mui/material/Link';



import Stack from '@mui/material/Stack';


import Dialog from '@mui/material/Dialog';
import DialogActions from '@mui/material/DialogActions';
import DialogContent from '@mui/material/DialogContent';
import DialogContentText from '@mui/material/DialogContentText';
import DialogTitle from '@mui/material/DialogTitle';


export default function Home() {

    const baseURL = 'http://localhost:8000'
    const psm_a = [] //最后需要生成的口算题参数数组
    const [psm_info, setpsm_info] = useState('');

    // 弹出信息图是窗口
    const [psmalert, setPsmalert] = useState(false);
    const handlepsmalertClose = () => {
        setPsmalert(false);
    };

    // 弹出更多设置窗口
    const [psmopen, setPsmopen] = useState(false);
    const handleClickpsmOpen = () => {
        setPsmopen(true);
    };
    const handlepsmClose = () => {
        setPsmopen(false);
    };

    // 几步运算
    const [step, setStep] = useState(1)
    const handleStepChange = (e) => {
        let k = e.target.value
        setStep(k)
        // 多步运算时ui组件的展示与隐藏
        if (k == 1) {
            setSyb("none")
            setSyc("none")
        }
        else if (k == 2) {
            setSyc("none")
            setSyb("flex")
        } else if (k == 3) {
            setSyc("flex")
            setSyb("flex")
        }
    }

    // 题型设置
    const [is_result, setis_result] = useState(1)
    const handleIsResultChange = (e) => {
        setis_result(e.target.value)
    }

    // 启用括号
    const [is_bracket, setIs_bracket] = useState(false)
    const handleis_bracketChange = (e) => {
        setIs_bracket(e.target.checked)
    }

    // 加法设置
    const [carry, setCarry] = useState(1)
    const handleCarryChange = (e) => {
        setCarry(e.target.value)
    }


    // 减法法设置
    const [abdication, setAbdication] = useState(1)
    const handleAbdicationChange = (e) => {
        setAbdication(e.target.value)
    }

    // 除法法设置
    const [remainder, setRemainder] = useState(2)
    const handleRemainderChange = (e) => {
        setRemainder(e.target.value)
    }

    // -----------------------------------

    // 算数项取值

    const [multistep_a1, setMultistep_a1] = useState("1")
    const handleMultistep_a1Change = (e) => {
        setMultistep_a1(e.target.value)
    }

    const [multistep_a2, setMultistep_a2] = useState("9")
    const handleMultistep_a2Change = (e) => {
        setMultistep_a2(e.target.value)
    }

    const [multistep_b1, setMultistep_b1] = useState("1")
    const handleMultistep_b1Change = (e) => {
        setMultistep_b1(e.target.value)
    }

    const [multistep_b2, setMultistep_b2] = useState("9")
    const handleMultistep_b2Change = (e) => {
        setMultistep_b2(e.target.value)
    }

    const [multistep_c1, setMultistep_c1] = useState("1")
    const handleMultistep_c1Change = (e) => {
        setMultistep_c1(e.target.value)
    }

    const [multistep_c2, setMultistep_c2] = useState("9")
    const handleMultistep_c2Change = (e) => {
        setMultistep_c2(e.target.value)
    }

    const [multistep_d1, setMultistep_d1] = useState("1")
    const handleMultistep_d1Change = (e) => {
        setMultistep_d1(e.target.value)
    }

    const [multistep_d2, setMultistep_d2] = useState("9")
    const handleMultistep_d2Change = (e) => {
        setMultistep_d2(e.target.value)
    }

    const [multistep_e1, setMultistep_e1] = useState("1")
    const handleMultistep_e1Change = (e) => {
        setMultistep_e1(e.target.value)
    }

    const [multistep_e2, setMultistep_e2] = useState("9")
    const handleMultistep_e2Change = (e) => {
        setMultistep_e2(e.target.value)
    }

    // -----------------------------------
    // 多步运算时的符号选择

    // 第1步运算符号
    const [symbols_a1, setSymbols_a1] = useState(true)
    const handleSymbols_a1Change = (e) => {
        setSymbols_a1(e.target.checked)
    }

    const [symbols_a2, setSymbols_a2] = useState(false)
    const handleSymbols_a2Change = (e) => {
        setSymbols_a2(e.target.checked)
    }

    const [symbols_a3, setSymbols_a3] = useState(false)
    const handleSymbols_a3Change = (e) => {
        setSymbols_a3(e.target.checked)
    }

    const [symbols_a4, setSymbols_a4] = useState(false)
    const handleSymbols_a4Change = (e) => {
        setSymbols_a4(e.target.checked)
    }

    // 第2步运算符号
    const [symbols_b1, setSymbols_b1] = useState(true)
    const handleSymbols_b1Change = (e) => {
        setSymbols_b1(e.target.checked)
    }

    const [symbols_b2, setSymbols_b2] = useState(false)
    const handleSymbols_b2Change = (e) => {
        setSymbols_b2(e.target.checked)
    }

    const [symbols_b3, setSymbols_b3] = useState(false)
    const handleSymbols_b3Change = (e) => {
        setSymbols_b3(e.target.checked)
    }

    const [symbols_b4, setSymbols_b4] = useState(false)
    const handleSymbols_b4Change = (e) => {
        setSymbols_b4(e.target.checked)
    }

    // 第3步运算符号
    const [symbols_c1, setSymbols_c1] = useState(true)
    const handleSymbols_c1Change = (e) => {
        setSymbols_c1(e.target.checked)
    }

    const [symbols_c2, setSymbols_c2] = useState(false)
    const handleSymbols_c2Change = (e) => {
        setSymbols_c2(e.target.checked)
    }

    const [symbols_c3, setSymbols_c3] = useState(false)
    const handleSymbols_c3Change = (e) => {
        setSymbols_c3(e.target.checked)
    }

    const [symbols_c4, setSymbols_c4] = useState(false)
    const handleSymbols_c4Change = (e) => {
        setSymbols_c4(e.target.checked)
    }


    // ----------------------------------------
    const [juanzishu, setJuanzishu] = useState("3")
    const handleJuanzishuChange = (e) => {
        setJuanzishu(e.target.value)
    }

    const [lieshu, setLieshu] = useState("4")
    const handleLieshuChange = (e) => {
        setLieshu(e.target.value)
    }

    const [jz_title, setJz_title] = useState("小学生口算题")
    const handleJz_titleChange = (e) => {
        setJz_title(e.target.value)
    }

    const [inf_title, setInf_title] = useState("姓名：__________ 日期：____月____日 时间：________ 对题：____道")
    const handleInf_titleChange = (e) => {
        setInf_title(e.target.value)
    }

    const [number, setNumber] = useState("30")
    const handleNumberChange = (e) => {
        setNumber(e.target.value)
    }

    const [psmtextarea, setPsmtextarea] = useState("")
    const handlePsmtextareaChange = (e) => {
        setPsmtextarea(e.target.value)
    }

    // ----------------------
    // 定义一些用来隐藏基本设置中运算符号和算数项的css display变量,根据几步运算来现实或隐藏.
    const [syb, setSyb] = useState("none") //第2步运算符号
    const [syc, setSyc] = useState("none") //第3步运算符号

    const handleCreatePSM = () => {
        /**
         * 创建一组口算题的配置（为当前口算题添加内容）
         */
        let psm_tmp = {}
        psm_tmp.step = step
        psm_tmp.number = number
        psm_tmp.is_result = is_result
        if (is_bracket) {
            psm_tmp.is_bracket = 1
        } else {
            psm_tmp.is_bracket = 0
        }

        psm_tmp.add = {
            "carry": carry
        }
        psm_tmp.sub = {
            "abdication": abdication
        }
        psm_tmp.mult = {}
        psm_tmp.div = {
            "remainder": remainder
        }

        // 算数项
        psm_tmp.multistep = [
            [parseInt(multistep_a1), parseInt(multistep_a2),],
            [parseInt(multistep_b1), parseInt(multistep_b2),],
            [parseInt(multistep_c1), parseInt(multistep_c2),],
            [parseInt(multistep_d1), parseInt(multistep_d2),],
            [parseInt(multistep_e1), parseInt(multistep_e2),]
        ]
        // 算数符号
        let ss_a = []
        symadd(ss_a, symbols_a1, 1); symadd(ss_a, symbols_a2, 2); symadd(ss_a, symbols_a3, 3); symadd(ss_a, symbols_a4, 4);
        let ss_b = []
        symadd(ss_b, symbols_b1, 1); symadd(ss_b, symbols_b2, 2); symadd(ss_b, symbols_b3, 3); symadd(ss_b, symbols_b4, 4);
        let ss_c = []
        symadd(ss_c, symbols_c1, 1); symadd(ss_c, symbols_c2, 2); symadd(ss_c, symbols_c3, 3); symadd(ss_c, symbols_c4, 4);
        psm_tmp.symbols = [ss_a, ss_b, ss_c]
        const json_data = JSON.stringify(psm_tmp)
        const tempdata = "dfsdfsdfdsf"
        // console.log(json_data)
        axios.get(baseURL + '/api_createpsm', {
            params: {
                json_data: json_data
            }
        },//{ headers: { 'Content-Type': 'application/json' } },
        ).then(function (res) {
            if (res.data.info != '0') {
                // console.log(res.data.info)
                let temptext = psmtextarea
                temptext += res.data.info
                psm_a.push(json_data)
                setPsmtextarea(temptext)
            } else {
                // console.log("口算题配置错误!")
                setpsm_info("口算题配置错误!") 
                setPsmalert(true)
            }
        }).catch(function (error) {
            console.log(error)
        })

    }

    const symadd = (arr, sym, int) => {
        if (sym) {
            arr.push(int)
        }
    }

    const cleartext = () => {
        // 清空所有口算题参数和提示窗口
        setPsmtextarea("")
        psm_a.length = 0
    }


    useEffect(() => {
        // 界面初始化
        // TODO 加载组件初始化的数据

    }, [])

    // 数据测试
    const handlTest = (e) => {
        // console.log(step, is_result, is_bracket)
        // console.log(carry, abdication, remainder)
        // console.log(multistep_a1, multistep_a2, multistep_b1, multistep_b2, multistep_c1, multistep_c2, multistep_d1, multistep_d2,
        //     multistep_e1, multistep_e2)
        // console.log(symbols_a1, symbols_a2, symbols_a3, symbols_a4)
        // console.log(symbols_b1, symbols_b2, symbols_b3, symbols_b4)
        // console.log(symbols_c1, symbols_c2, symbols_c3, symbols_c4)
        // console.log(juanzishu, lieshu, jz_title, inf_title, number, psmtextarea)
        // console.log(handleCreatePSM())
    }

    return (
        <Container component="main" >
            <Card sx={{ mx: "auto", my: 2, maxWidth: 600 }}>
                <CardMedia
                    component="img"
                    height="140"
                    image={img_01}
                    alt="green iguana"
                />
                <CardContent>
                    <Typography gutterBottom variant="h5" component="div">
                        程序参数设置
                    </Typography>
                    <Typography variant="body2" color="text.secondary">
                        如果您对程序的设置不太理解，请查阅帮助文档
                    </Typography>
                    <Box sx={{ flexGrow: 1, my: 1 }}>
                        <Grid container spacing={2}>
                            <Grid item xs={12} >
                                <Grid container spacing={2}>

                                    <Grid item xs={12}>
                                        <Box
                                            sx={{
                                                display: 'flex',
                                                alignItems: 'center',
                                                '& > :not(style)': { m: 1 },
                                                maxWidth: 660
                                            }}
                                        >
                                            <FormControl sx={{ m: 1, minWidth: 120 }} size="small">
                                                <InputLabel id="demo-select-small">几步运算?</InputLabel>
                                                <Select
                                                    labelId="demo-select-small"
                                                    id="demo-select-small"
                                                    value={step}
                                                    label="几步运算?"
                                                    onChange={handleStepChange}
                                                >
                                                    <MenuItem value={1}>一步运算</MenuItem>
                                                    <MenuItem value={2}>两步运算</MenuItem>
                                                    <MenuItem value={3}>三步运算</MenuItem>
                                                </Select>
                                            </FormControl>


                                            <Button variant="contained" color="success" onClick={handleClickpsmOpen}>
                                                其它程序参数设置
                                            </Button>
                                        </Box>
                                    </Grid>

                                </Grid>


                                <Grid item xs={12}>
                                    <Box
                                        sx={{
                                            display: 'flex',
                                            alignItems: 'center',
                                            '& > :not(style)': { m: 1 },
                                            maxWidth: 320
                                        }}
                                    >
                                        <TextField
                                            helperText="第1个算数项最小值"
                                            id="demo-helper-text-aligned"
                                            label="数值"
                                            size="small"
                                            value={multistep_a1}
                                            onChange={handleMultistep_a1Change}
                                        />

                                        <TextField
                                            helperText="第1个算数项最大值"
                                            id="demo-helper-text-aligned-no-helper"
                                            label="数值"
                                            size="small"
                                            value={multistep_a2}
                                            onChange={handleMultistep_a2Change}
                                        />
                                    </Box>
                                </Grid>
                                <Grid item xs={12}>
                                    <Box
                                        sx={{
                                            display: 'flex',
                                            alignItems: 'center',
                                            '& > :not(style)': { m: 1 },
                                            maxWidth: 555
                                        }}
                                    >
                                        <FormControl sx={{ m: 1, minWidth: 120 }} size="small">
                                            <FormLabel component="legend">第1步运算符号</FormLabel>
                                            <FormGroup aria-label="position" row>
                                                <FormControlLabel control={<Checkbox checked={symbols_a1} onChange={handleSymbols_a1Change} />} label="+(加法)" />
                                                <FormControlLabel control={<Checkbox checked={symbols_a2} onChange={handleSymbols_a2Change} />} label="-(减法)" />
                                                <FormControlLabel control={<Checkbox checked={symbols_a3} onChange={handleSymbols_a3Change} />} label="×(乘法)" />
                                                <FormControlLabel control={<Checkbox checked={symbols_a4} onChange={handleSymbols_a4Change} />} label="÷(除法)" />
                                            </FormGroup>
                                        </FormControl>
                                    </Box>
                                </Grid>
                                <Grid item xs={12}>
                                    <Box
                                        sx={{
                                            display: 'flex',
                                            alignItems: 'center',
                                            '& > :not(style)': { m: 1 },
                                            maxWidth: 320
                                        }}
                                    >
                                        <TextField
                                            helperText="第2个算数项最小值"
                                            id="demo-helper-text-aligned"
                                            label="数值"
                                            size="small"
                                            value={multistep_b1}
                                            onChange={handleMultistep_b1Change}
                                        />

                                        <TextField
                                            helperText="第2个算数项最大值"
                                            id="demo-helper-text-aligned-no-helper"
                                            label="数值"
                                            size="small"
                                            value={multistep_b2}
                                            onChange={handleMultistep_b2Change}
                                        />
                                    </Box>
                                </Grid>
                                <Grid item xs={12} display={syb}>
                                    <Box
                                        sx={{
                                            display: 'flex',
                                            alignItems: 'center',
                                            '& > :not(style)': { m: 1 },
                                            maxWidth: 555
                                        }}
                                    >
                                        <FormControl sx={{ m: 1, minWidth: 120 }} size="small">
                                            <FormLabel component="legend">第2步运算符号</FormLabel>
                                            <FormGroup aria-label="position" row>
                                                <FormControlLabel control={<Checkbox checked={symbols_b1} onChange={handleSymbols_b1Change} />} label="+(加法)" />
                                                <FormControlLabel control={<Checkbox checked={symbols_b2} onChange={handleSymbols_b2Change} />} label="-(减法)" />
                                                <FormControlLabel control={<Checkbox checked={symbols_b3} onChange={handleSymbols_b3Change} />} label="×(乘法)" />
                                                <FormControlLabel control={<Checkbox checked={symbols_b4} onChange={handleSymbols_b4Change} />} label="÷(除法)" />
                                            </FormGroup>
                                        </FormControl>
                                    </Box>
                                </Grid>
                                <Grid item xs={12} display={syb}>
                                    <Box
                                        sx={{
                                            display: 'flex',
                                            alignItems: 'center',
                                            '& > :not(style)': { m: 1 },
                                            maxWidth: 320
                                        }}
                                    >
                                        <TextField
                                            helperText="第3个算数项最小值"
                                            id="demo-helper-text-aligned"
                                            label="数值"
                                            size="small"
                                            value={multistep_c1}
                                            onChange={handleMultistep_c1Change}
                                        />

                                        <TextField
                                            helperText="第3个算数项最大值"
                                            id="demo-helper-text-aligned-no-helper"
                                            label="数值"
                                            size="small"
                                            value={multistep_c2}
                                            onChange={handleMultistep_c2Change}
                                        />
                                    </Box>
                                </Grid>
                                <Grid item xs={12} display={syc}>
                                    <Box
                                        sx={{
                                            display: 'flex',
                                            alignItems: 'center',
                                            '& > :not(style)': { m: 1 },
                                            maxWidth: 555
                                        }}
                                    >
                                        <FormControl sx={{ m: 1, minWidth: 120 }} size="small">
                                            <FormLabel component="legend">第3处运算符号</FormLabel>
                                            <FormGroup aria-label="position" row>
                                                <FormControlLabel control={<Checkbox checked={symbols_c1} onChange={handleSymbols_c1Change} />} label="+(加法)" />
                                                <FormControlLabel control={<Checkbox checked={symbols_c2} onChange={handleSymbols_c2Change} />} label="-(减法)" />
                                                <FormControlLabel control={<Checkbox checked={symbols_c3} onChange={handleSymbols_c3Change} />} label="×(乘法)" />
                                                <FormControlLabel control={<Checkbox checked={symbols_c4} onChange={handleSymbols_c4Change} />} label="÷(除法)" />
                                            </FormGroup>
                                        </FormControl>
                                    </Box>
                                </Grid>
                                <Grid item xs={12} display={syc}>
                                    <Box
                                        sx={{
                                            display: 'flex',
                                            alignItems: 'center',
                                            '& > :not(style)': { m: 1 },
                                            maxWidth: 320
                                        }}
                                    >
                                        <TextField
                                            helperText="第4个算数项最小值"
                                            id="demo-helper-text-aligned"
                                            label="数值"
                                            size="small"
                                            value={multistep_d1}
                                            onChange={handleMultistep_d1Change}
                                        />

                                        <TextField
                                            helperText="第4个算数项最大值"
                                            id="demo-helper-text-aligned-no-helper"
                                            label="数值"
                                            size="small"
                                            value={multistep_d2}
                                            onChange={handleMultistep_d2Change}
                                        />
                                    </Box>
                                </Grid>
                                <Grid item xs={12}>
                                    <Box
                                        sx={{
                                            display: 'flex',
                                            alignItems: 'center',
                                            '& > :not(style)': { m: 1 },
                                            maxWidth: 320
                                        }}
                                    >
                                        <TextField
                                            helperText="运算结果最小值"
                                            id="demo-helper-text-aligned"
                                            label="数值"
                                            size="small"
                                            value={multistep_e1}
                                            onChange={handleMultistep_e1Change}
                                        />

                                        <TextField
                                            helperText="运算结果最大值"
                                            id="demo-helper-text-aligned-no-helper"
                                            label="数值"
                                            size="small"
                                            value={multistep_e2}
                                            onChange={handleMultistep_e2Change}
                                        />
                                    </Box>
                                </Grid>
                            </Grid>

                        </Grid>
                    </Box>
                </CardContent>
                <CardActions>
                    <Box sx={{ flexGrow: 1, my: 1, '& button': { ml: 0.5, mt: 0.2 } }}>
                        <Grid container spacing={2}>
                            <Grid item xs={12} >
                                <TextField
                                    id="demo-helper-text-aligned-no-helper"
                                    label="口算题数量"
                                    size="small"
                                    value={number}
                                    onChange={handleNumberChange}
                                />

                                <Button variant="contained" size="medium" onClick={handleCreatePSM}  >添加口算题</Button>
                                <Button variant="contained" size="medium" onClick={cleartext} >清空口算题</Button>


                            </Grid>
                        </Grid>
                        <Grid item xs={12} >
                            <TextField
                                fullWidth
                                id="outlined-multiline-static"
                                label="当前口算题包含内容"
                                multiline
                                rows={2}
                                value={psmtextarea}
                                onChange={handlePsmtextareaChange}
                            />
                            <Stack spacing={2}><Button variant="contained" size="medium"  >点此生成口算题</Button></Stack>
                            {/* <Button size="small" onClick={handlTest} >测试数据</Button> */}
                        </Grid>
                    </Box>
                </CardActions>
            </Card>

            <Dialog
                open={psmopen}
                keepMounted
                onClose={handlepsmClose}
                aria-labelledby="alert-dialog-title"
                aria-describedby="alert-dialog-description"
            >
                <DialogTitle>{"其它程序参数设置"}</DialogTitle>
                <DialogContent>

                    <Grid container spacing={2} sx={{ p: 2, }} >
                        <Grid item xs={6}>
                            <Box
                                sx={{
                                    display: 'flex',
                                    alignItems: 'center',
                                    '& > :not(style)': { m: 1 },
                                    maxWidth: 660
                                }}
                            >
                                <FormControl sx={{ m: 1, minWidth: 120 }} size="small">
                                    <InputLabel id="demo-is_result-small">题型设置</InputLabel>
                                    <Select
                                        labelId="demo-select-small"
                                        id="demo-is_result-small"
                                        value={is_result}
                                        label="题型设置"
                                        onChange={handleIsResultChange}
                                    >
                                        <MenuItem value={1}>求结果</MenuItem>
                                        <MenuItem value={2}>求算数项</MenuItem>
                                    </Select>
                                </FormControl>
                                <FormGroup>
                                    <FormControlLabel control={<Switch
                                        checked={is_bracket}
                                        onChange={handleis_bracketChange}
                                    />}
                                        labelPlacement="end"
                                        label="启用括号( )"
                                        sx={{ m: 1, minWidth: 240 }}
                                    />
                                </FormGroup>
                            </Box>
                        </Grid>
                    </Grid>
                    <Grid container spacing={2} sx={{ p: 2, }}>
                        <Grid item xs={4}>
                            <FormControl sx={{ m: 1, minWidth: 120 }} size="small">
                                <InputLabel id="demo-carry-small">加法设置</InputLabel>
                                <Select
                                    labelId="demo-carry-small"
                                    id="demo-carry-small"
                                    value={carry}
                                    label="加法设置"
                                    onChange={handleCarryChange}
                                >
                                    <MenuItem value={1}>随机进位</MenuItem>
                                    <MenuItem value={2}>加法进位</MenuItem>
                                    <MenuItem value={3}>没有进位</MenuItem>

                                </Select>
                            </FormControl>
                        </Grid>
                        <Grid item xs={4}>
                            <FormControl sx={{ m: 1, minWidth: 120 }} size="small">
                                <InputLabel id="demo-sabdication-small">减法设置</InputLabel>
                                <Select
                                    labelId="demo-abdication-small"
                                    id="demo-abdication-small"
                                    value={abdication}
                                    label="减法设置"
                                    onChange={handleAbdicationChange}
                                >
                                    <MenuItem value={1}>随机退位</MenuItem>
                                    <MenuItem value={2}>加法退位</MenuItem>
                                    <MenuItem value={3}>没有退位</MenuItem>

                                </Select>
                            </FormControl>
                        </Grid>
                        <Grid item xs={4}>
                            <FormControl sx={{ m: 1, minWidth: 120 }} size="small">
                                <InputLabel id="demo-remainder-small">除法设置</InputLabel>
                                <Select
                                    labelId="demo-remainder-small"
                                    id="demo-remainder-small"
                                    value={remainder}
                                    label="除法设置"
                                    onChange={handleRemainderChange}
                                >
                                    <MenuItem value={1}>随机有余数</MenuItem>
                                    <MenuItem value={2}>结果整除</MenuItem>
                                    <MenuItem value={3}>结果有余数</MenuItem>

                                </Select>
                            </FormControl>
                        </Grid>

                    </Grid>
                    <Grid container spacing={2} sx={{ p: 2, }}>
                        <Grid item xs={12}>
                            <Box
                                sx={{
                                    display: 'flex',
                                    alignItems: 'center',
                                    '& > :not(style)': { m: 1 },
                                    maxWidth: 622
                                }}
                            >
                                <TextField

                                    id="demo-helper-text-aligned"
                                    label="生成的卷子数量"
                                    size="small"
                                    value={juanzishu}
                                    onChange={handleJuanzishuChange}
                                />

                                <TextField

                                    id="demo-helper-text-aligned-no-helper"
                                    label="口算题列数"
                                    size="small"
                                    value={lieshu}
                                    onChange={handleLieshuChange}
                                />
                                <TextField

                                    id="demo-helper-text-aligned-no-helper"
                                    label="卷子标题"
                                    size="small"
                                    value={jz_title}
                                    onChange={handleJz_titleChange}
                                />
                            </Box>
                        </Grid>
                        <Grid item xs={12}>
                            <Box
                                sx={{
                                    display: 'flex',
                                    alignItems: 'center',
                                    '& > :not(style)': { m: 1 },
                                    maxWidth: 622
                                }}
                            >
                                <TextField
                                    fullWidth
                                    id="demo-helper-text-aligned-no-helper"
                                    label="卷子副标题"
                                    size="small"
                                    value={inf_title}
                                    onChange={handleInf_titleChange}
                                />
                            </Box>
                        </Grid>
                    </Grid>

                </DialogContent>
                <DialogActions>

                    <Button onClick={handlepsmClose}>完成</Button>
                </DialogActions>
            </Dialog>

            {/* 消息警告提示 */}
            <Dialog
                open={psmalert}
                onClose={handlepsmalertClose}
                aria-labelledby="alert-dialog-title"
                aria-describedby="alert-dialog-description"
            >
                <DialogTitle id="alert-dialog-title">
                    {"提示信息"}
                </DialogTitle>
                <DialogContent>
                    <DialogContentText id="alert-dialog-description">
                        {psm_info}
                    </DialogContentText>
                </DialogContent>
                <DialogActions>
                    
                    <Button onClick={handlepsmalertClose} autoFocus>
                        确认关闭
                    </Button>
                </DialogActions>
            </Dialog>

            <Box
                sx={{
                    alignItems: 'center',
                    width: '100%',
                    mx: "auto", my: 1, maxWidth: 600
                }}
            >
                <Typography variant="body2" gutterBottom display="block">
                    孩子上小学一年级了，加减乘除的口算就要开始练习了，估计老师肯定会让家长出题，所以提前准备一下，利用Python开发了一套自动生成小学生口算题的小应用。
                    为了让程序员老爹解放抄题的双手，让你拥有更多的时间去写代码而不用去手写几道口算题而伤神伤脑。
                    所以有或没有娃子的程序员爹爹加入一起来继续优化这个开源小程序的？有什么点子，发现什么BUG，欢迎提出issue。
                    仅以此软件，献给那些热爱Python、热爱生活、热爱孩子的程序员老爹们！
                </Typography>

                <Typography variant="overline" display="block" gutterBottom>
                    本程序源码仓库:

                </Typography>
                <Typography variant="overline" display="block" gutterBottom>
                    <Link href="https://gitee.com/J_Sky/PrimarySchoolMathematics" color="inherit">
                        国内码云
                    </Link>
                </Typography>
                <Typography variant="overline" display="block" gutterBottom>
                    <Link href="https://github.com/bosichong/PrimarySchoolMathematics" color="inherit">
                        Github
                    </Link>
                </Typography>


            </Box>
        </Container>
    );
}

