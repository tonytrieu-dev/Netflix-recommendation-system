import { useState } from 'react';
import { Container, Typography, Alert, Box, CircularProgress } from '@mui/material';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import SearchBar from './components/SearchBar/SearchBar';
import RecommendationList from './components/RecommendationList/RecommendationList';
import { getRecommendations, MovieRecommendation } from './services/api';

const darkTheme = createTheme({
  palette: {
    mode: 'dark',
    primary: {
      main: '#1976d2', 
    },
    background: {
      default: '#141414',
      paper: '#141414',
    },
  },
  typography: {
    fontFamily: [
      'Netflix Sans',
      '-apple-system',
      'BlinkMacSystemFont',
      '"Segoe UI"',
      'Roboto',
      '"Helvetica Neue"',
      'Arial',
      'sans-serif',
    ].join(','),
    h3: {
      fontFamily: [
        '-apple-system',
        'BlinkMacSystemFont',
        '"Segoe UI"',
        'Roboto',
        '"Helvetica Neue"',
        'Arial',
        'sans-serif',
      ].join(','),
    },
    body1: {
      fontSize: '1rem',
      letterSpacing: '0.00938em',
    },
    button: {
      textTransform: 'none',
      fontWeight: 500,
    },
  },
  components: {
    MuiInputBase: {
      styleOverrides: {
        root: {
          fontFamily: 'Netflix Sans, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif',
        },
      },
    },
    MuiMenuItem: {
      styleOverrides: {
        root: {
          fontFamily: 'Netflix Sans, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif',
          fontSize: '1rem',
        },
      },
    },
  },
});

function App() {
  const [recommendations, setRecommendations] = useState<MovieRecommendation[]>([]);
  const [error, setError] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [currentContentType, setCurrentContentType] = useState('shows');  

  const handleSearch = async (title: string, contentType: string, count: number) => {
    setIsLoading(true);
    setError(null);
    setCurrentContentType(contentType);  
    
    try {
      const results = await getRecommendations(title, contentType, count);
      setRecommendations(results);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An unexpected error occurred');
      setRecommendations([]);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <ThemeProvider theme={darkTheme}>
      <CssBaseline />
      <Container maxWidth="lg" className="app-container">
        <Box sx={{ py: 4 }}>
          <Typography
            variant="h3"
            component="h1"
            align="center"
            gutterBottom
            sx={{
              fontWeight: 600,
              color: '#ffffff',
              textShadow: '2px 2px 4px rgba(0,0,0,0.5)',
            }}
          >
            Netflix Content Recommender
          </Typography>

          <Box sx={{ maxWidth: 800, mx: 'auto', mb: 5 }}>
            <SearchBar onSearch={handleSearch} isLoading={isLoading} />
          </Box>

          {error && (
            <Alert
              severity="error"
              sx={{
                mb: 2,
                backgroundColor: 'rgba(25, 118, 210, 0.1)', 
                color: '#64b5f6', 
              }}
            >
              {error}
            </Alert>
          )}

          {isLoading && (
            <Box sx={{ display: 'flex', justifyContent: 'center', my: 4 }}>
              <CircularProgress sx={{ color: '#1976d2' }} /> 
            </Box>
          )}

          {recommendations.length > 0 && (
            <RecommendationList 
              recommendations={recommendations}
              contentType={currentContentType}  
            />
          )}
        </Box>
      </Container>
    </ThemeProvider>
  );
}

export default App;
