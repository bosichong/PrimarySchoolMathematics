import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import Typography from '@mui/material/Typography';
import Link from '@mui/material/Link';

// 页面底部
export default function Footer(){
    return(
        <Card sx={{ mx: "auto", my: 2, maxWidth: 600 }}>

                <CardContent>
                    <Typography gutterBottom variant="body2" component="div">
                        <img alt="python-3.8.8" src="https://img.shields.io/badge/Python-3.8.8-green?logo=python" />
                        <img alt="fastAPI-0.85.1" src="https://img.shields.io/badge/fastAPI-0.85.1-green" />
                        <img alt="React-18.2.0" src="https://img.shields.io/badge/React-18.2.0-blue" />
                        <img alt="Material UI-5.10.11" src="https://img.shields.io/badge/Material UI-5.10.11-blue" />
                        <img alt="license-Apache--2.0" src="https://img.shields.io/badge/license-Apache--2.0-green" />
                    </Typography>
                    <Typography variant="body2" color="text.secondary">
                        <Link href="https://gitee.com/J_Sky/PrimarySchoolMathematics" color="inherit">
                            <img alt="" src="https://img.shields.io/badge/Gitee--PrimarySchoolMathematics-red?logo=gitee" />
                        </Link>

                        <Link href="https://github.com/bosichong/PrimarySchoolMathematics" color="inherit">
                            <img alt="" src="https://img.shields.io/badge/Github--PrimarySchoolMathematics-green?logo=github" />
                        </Link>
                    </Typography>
                </CardContent>

            </Card>
    )
}