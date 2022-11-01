import img_01 from '../img_01.jpeg'
import React from 'react';
import cookie from 'react-cookies'
import axios from 'axios';
import { useState, useEffect } from 'react';
import { useNavigate } from "react-router-dom"
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';

import { styled } from '@mui/material/styles';
import Box from '@mui/material/Box';
import Paper from '@mui/material/Paper';
import Grid from '@mui/material/Grid';

import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';

import FormGroup from '@mui/material/FormGroup';
import FormControlLabel from '@mui/material/FormControlLabel';
import Switch from '@mui/material/Switch';
import TextField from '@mui/material/TextField';
import Divider from '@mui/material/Divider';



import ArrowForwardIosSharpIcon from '@mui/icons-material/ArrowForwardIosSharp';
import MuiAccordion from '@mui/material/Accordion';
import MuiAccordionSummary from '@mui/material/AccordionSummary';
import MuiAccordionDetails from '@mui/material/AccordionDetails';


export default function Home() {

    const baseURL = 'http://localhost:8000'

    // 运算类型选择

    const [signum, setSignum] = useState(1)
    const handleSignumChange = (e) => {
        setSignum(e.target.value)
    }

    // 几步运算
    const [step, setStep] = useState(1)
    const handleStepChange = (e) => {
        setStep(e.target.value)
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

    // 抽屉

    const Accordion = styled((props) => (
        <MuiAccordion disableGutters elevation={0} square {...props} />
    ))(({ theme }) => ({
        border: `1px solid ${theme.palette.divider}`,
        '&:not(:last-child)': {
            borderBottom: 0,
        },
        '&:before': {
            display: 'none',
        },
    }));

    const AccordionSummary = styled((props) => (
        <MuiAccordionSummary
            expandIcon={<ArrowForwardIosSharpIcon sx={{ fontSize: '0.9rem' }} />}
            {...props}
        />
    ))(({ theme }) => ({
        backgroundColor:
            theme.palette.mode === 'dark'
                ? 'rgba(255, 255, 255, .05)'
                : 'rgba(0, 0, 0, .03)',
        flexDirection: 'row-reverse',
        '& .MuiAccordionSummary-expandIconWrapper.Mui-expanded': {
            transform: 'rotate(90deg)',
        },
        '& .MuiAccordionSummary-content': {
            marginLeft: theme.spacing(1),
        },
    }));

    const AccordionDetails = styled(MuiAccordionDetails)(({ theme }) => ({
        padding: theme.spacing(2),
        borderTop: '1px solid rgba(0, 0, 0, .125)',
    }));
    // 默认展开panel1
    const [expanded, setExpanded] = React.useState('panel2');
    const handleChange = (panel) => (event, newExpanded) => {
        setExpanded(newExpanded ? panel : false);
    };


    // 加法设置
    const [carry, setCarry] = useState(1)
    const handleCarryChange = (e) => {
        setCarry(e.target.value)
    }

    // 数据测试
    const handlTest = (e) => {
        console.log("运算类型:"+signum)
        console.log(step)
        console.log(is_result)
        console.log(is_bracket)
        console.log(carry)
    }

    return (
        <Container component="main" >
            <Card sx={{ mx: "auto", my: 2, maxWidth: 666 }}>
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
                                <div>
                                    <Accordion expanded={expanded === 'panel1'} onChange={handleChange('panel1')}>
                                        <AccordionSummary aria-controls="panel1d-content" id="panel1d-header">
                                            <Typography>口算题基本设置</Typography>
                                        </AccordionSummary>
                                        <AccordionDetails>
                                            
                                                <Grid container spacing={2}>
                                                    <Grid item xs={3}>
                                                        <FormControl sx={{ m: 1, minWidth: 120 }} size="small">
                                                            <InputLabel id="demo-select-small">运算类型</InputLabel>
                                                            <Select
                                                                labelId="demo-select-small"
                                                                id="demo-select-small"
                                                                value={signum}
                                                                label="Signum"
                                                                onChange={handleSignumChange}
                                                            >
                                                                <MenuItem value={1}>加法</MenuItem>
                                                                <MenuItem value={2}>减法</MenuItem>
                                                                <MenuItem value={3}>乘法</MenuItem>
                                                                <MenuItem value={4}>除法</MenuItem>
                                                            </Select>
                                                        </FormControl>
                                                    </Grid>
                                                    <Grid item xs={3}>
                                                        <FormControl sx={{ m: 1, minWidth: 120 }} size="small">
                                                            <InputLabel id="demo-select-small">几步运算</InputLabel>
                                                            <Select
                                                                labelId="demo-select-small"
                                                                id="demo-select-small"
                                                                value={step}
                                                                label="Step"
                                                                onChange={handleStepChange}
                                                            >
                                                                <MenuItem value={1}>一步</MenuItem>
                                                                <MenuItem value={2}>两步</MenuItem>
                                                                <MenuItem value={3}>三步</MenuItem>
                                                            </Select>
                                                        </FormControl>

                                                    </Grid>
                                                    <Grid item xs={3}>
                                                        <FormControl sx={{ m: 1, minWidth: 120 }} size="small">
                                                            <InputLabel id="demo-select-small">题型设置</InputLabel>
                                                            <Select
                                                                labelId="demo-select-small"
                                                                id="demo-select-small"
                                                                value={is_result}
                                                                label="is_result"
                                                                onChange={handleIsResultChange}
                                                            >
                                                                <MenuItem value={1}>求结果</MenuItem>
                                                                <MenuItem value={2}>求算数项</MenuItem>
                                                            </Select>
                                                        </FormControl>
                                                    </Grid>
                                                    <Grid item xs={3}>
                                                        <FormGroup>
                                                            <FormControlLabel control={<Switch
                                                                checked={is_bracket}
                                                                onChange={handleis_bracketChange}
                                                            />}
                                                                label="启用括号"
                                                            />
                                                        </FormGroup>
                                                    </Grid>
                                                </Grid>
                                            
                                        </AccordionDetails>
                                    </Accordion>
                                    <Accordion expanded={expanded === 'panel2'} onChange={handleChange('panel2')}>
                                        <AccordionSummary aria-controls="panel2d-content" id="panel2d-header">
                                            <Typography>加减乘除法设置</Typography>
                                        </AccordionSummary>
                                        <AccordionDetails>
                                            
                                                <Grid container spacing={2}>
                                                    <Grid item xs={3}>
                                                        <FormControl sx={{ m: 1, minWidth: 120 }} size="small">
                                                            <InputLabel id="demo-select-small">加法设置</InputLabel>
                                                            <Select
                                                                labelId="demo-select-small"
                                                                id="demo-select-small"
                                                                value={carry}
                                                                label="carry"
                                                                onChange={handleCarryChange}
                                                            >
                                                                <MenuItem value={1}>随机进位</MenuItem>
                                                                <MenuItem value={2}>加法进位</MenuItem>
                                                                <MenuItem value={3}>没有进位</MenuItem>

                                                            </Select>
                                                        </FormControl>
                                                    </Grid>
                                                    <Grid item xs={3}>
                                                        

                                                    </Grid>
                                                    <Grid item xs={3}>
                                                        
                                                    </Grid>
                                                    <Grid item xs={3}>
                                                       
                                                    </Grid>
                                                </Grid>
                                            
                                        </AccordionDetails>
                                    </Accordion>
                                    <Accordion expanded={expanded === 'panel3'} onChange={handleChange('panel3')}>
                                        <AccordionSummary aria-controls="panel3d-content" id="panel3d-header">
                                            <Typography>Collapsible Group Item #3</Typography>
                                        </AccordionSummary>
                                        <AccordionDetails>
                                            <Typography>
                                                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse
                                                malesuada lacus ex, sit amet blandit leo lobortis eget. Lorem ipsum dolor
                                                sit amet, consectetur adipiscing elit. Suspendisse malesuada lacus ex,
                                                sit amet blandit leo lobortis eget.
                                            </Typography>
                                        </AccordionDetails>
                                    </Accordion>
                                    <Accordion expanded={expanded === 'panel4'} onChange={handleChange('panel4')}>
                                        <AccordionSummary aria-controls="panel4d-content" id="panel4d-header">
                                            <Typography>Collapsible Group Item #4</Typography>
                                        </AccordionSummary>
                                        <AccordionDetails>
                                            
                                                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse
                                                malesuada lacus ex, sit amet blandit leo lobortis eget. Lorem ipsum dolor
                                                sit amet, consectetur adipiscing elit. Suspendisse malesuada lacus ex,
                                                sit amet blandit leo lobortis eget.
                                            
                                        </AccordionDetails>
                                    </Accordion>
                                </div>
                            </Grid>
                        </Grid>
                    </Box>
                </CardContent>
                <CardActions>
                    <Button size="small" onClick={handlTest} >测试数据</Button>
                </CardActions>
            </Card>
        </Container>
    );
}

