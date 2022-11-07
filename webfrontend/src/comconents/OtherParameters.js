

import Button from '@mui/material/Button';
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';
import FormGroup from '@mui/material/FormGroup';
import FormControlLabel from '@mui/material/FormControlLabel';
import TextField from '@mui/material/TextField';
import Switch from '@mui/material/Switch';
import Dialog from '@mui/material/Dialog';
import DialogActions from '@mui/material/DialogActions';
import DialogContent from '@mui/material/DialogContent';
import DialogTitle from '@mui/material/DialogTitle';

// 其他参数设置模块
export default function OtherParameters(props){
    return (
        <Dialog
                open={props.psmopen}
                keepMounted
                onClose={props.handlepsmClose}
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
                                        value={props.is_result}
                                        label="题型设置"
                                        onChange={props.handleIsResultChange}
                                    >
                                        <MenuItem value={0}>求结果</MenuItem>
                                        <MenuItem value={1}>求算数项</MenuItem>
                                    </Select>
                                </FormControl>
                                <FormGroup>
                                    <FormControlLabel control={<Switch
                                        checked={props.is_bracket}
                                        onChange={props.handleis_bracketChange}
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
                                    value={props.carry}
                                    label="加法设置"
                                    onChange={props.handleCarryChange}
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
                                    value={props.abdication}
                                    label="减法设置"
                                    onChange={props.handleAbdicationChange}
                                >
                                    <MenuItem value={1}>随机退位</MenuItem>
                                    <MenuItem value={2}>减法退位</MenuItem>
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
                                    value={props.remainder}
                                    label="除法设置"
                                    onChange={props.handleRemainderChange}
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
                                    value={props.juanzishu}
                                    onChange={props.handleJuanzishuChange}
                                />

                                <TextField

                                    id="demo-helper-text-aligned-no-helper"
                                    label="口算题列数"
                                    size="small"
                                    value={props.lieshu}
                                    onChange={props.handleLieshuChange}
                                />
                                <TextField

                                    id="demo-helper-text-aligned-no-helper"
                                    label="卷子标题"
                                    size="small"
                                    value={props.jz_title}
                                    onChange={props.handleJz_titleChange}
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
                                    value={props.inf_title}
                                    onChange={props.handleInf_titleChange}
                                />
                            </Box>
                        </Grid>
                    </Grid>

                </DialogContent>
                <DialogActions>
                    <Button onClick={props.handlepsmClose}>完成</Button>
                </DialogActions>
            </Dialog>
    )
}