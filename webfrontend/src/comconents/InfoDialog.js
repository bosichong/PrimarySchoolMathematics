import Dialog from '@mui/material/Dialog';
import DialogActions from '@mui/material/DialogActions';
import DialogContent from '@mui/material/DialogContent';
import DialogContentText from '@mui/material/DialogContentText';
import DialogTitle from '@mui/material/DialogTitle';
import Button from '@mui/material/Button';


// 信息提示窗
export default function InfoDialog(props) {
    return (
        <Dialog
            fullWidth
            maxWidth={'xs'}
            open={props.psmalert}
            onClose={props.handlepsmalertClose}
            aria-labelledby="alert-dialog-title"
            aria-describedby="alert-dialog-description"
        >
            <DialogTitle id="alert-dialog-title">
                {"提示信息"}
            </DialogTitle>
            <DialogContent>
                <DialogContentText id="alert-dialog-description">
                    {props.psm_info}
                </DialogContentText>
            </DialogContent>
            <DialogActions>

                <Button onClick={props.handlepsmalertClose} autoFocus>
                    确认关闭
                </Button>
            </DialogActions>
        </Dialog>
    )
}