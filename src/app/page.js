// Bibliotecas externas
import Box from '@mui/material/Box'
import Typography from '@mui/material/Typography'
// Bibliotecas/utilitários internos
//
// Componentes
//
// Stylesheets
//

export default function Page() {
    return (
        <Box
            sx={{
                pt: 5,
                flexGrow: 1, // Box grows and takes up all the space, pushing ChatInput down
                display: 'flex',
                flexDirection: 'column',
                alignItems: 'center', // Centraliza o conteúdo horizontalmente
            }}
        >
            <Box
                sx={{
                    maxWidth: 600,
                    p: 1.3,
                    border: 1,
                    borderColor: 'border.primary',
                    borderRadius: 1,
                    backgroundColor: 'background.paper',
                    position: 'relative',
                    textAlign: 'center', // Centraliza o conteúdo dentro do box
                    margin: '0 auto', // Centraliza o box na tela
                }}
            >
                <Typography variant="h6">Hi there... 👋</Typography>
            </Box>
        </Box>
    )
}
