import { useState, KeyboardEvent } from 'react';
import { TextField, InputAdornment, IconButton, Box, Select, MenuItem, FormControl, InputLabel, CircularProgress, SelectChangeEvent } from '@mui/material';
import SearchIcon from '@mui/icons-material/Search';
import { styled } from '@mui/material/styles';

const StyledTextField = styled(TextField)(() => ({
  '& .MuiInputBase-root': {
    color: 'white',
    backgroundColor: '#333',
    borderRadius: '4px',
    height: '56px',
    fontSize: '1rem',
    fontWeight: 400,
    '&:hover': {
      backgroundColor: '#404040',
    },
    '& fieldset': {
      borderColor: 'transparent',
    },
    '&:hover fieldset': {
      borderColor: 'transparent',
    },
    '&.Mui-focused fieldset': {
      borderColor: '#0096FF',
    },
  },
  '& .MuiInputBase-input': {
    padding: '16px 14px',
  },
  flex: '1 1 auto', // Allow the text field to grow and fill space
}));

const StyledSelect = styled(Select)(() => ({
  height: '56px',
  fontSize: '1rem',
  fontWeight: 400,
  backgroundColor: '#333',
  color: 'white',
  '& .MuiSelect-select': {
    padding: '16px 14px',
  },
  '& .MuiOutlinedInput-notchedOutline': {
    borderColor: 'transparent',
  },
  '&:hover': {
    backgroundColor: '#404040',
  },
  '&:hover .MuiOutlinedInput-notchedOutline': {
    borderColor: 'transparent',
  },
  '&.Mui-focused .MuiOutlinedInput-notchedOutline': {
    borderColor: '#0096FF',
  },
  '& .MuiSelect-icon': {
    color: 'rgba(255, 255, 255, 0.54)',
  },
}));

const StyledFormControl = styled(FormControl)(() => ({
  minWidth: '200px',
  flex: '0 0 200px',
  '& .MuiInputLabel-root': {
    transform: 'translate(14px, -20px) scale(0.75)',
    '&.Mui-focused': {
      color: '#1976d2',
    }
  },
  '& .MuiOutlinedInput-notchedOutline': {
    borderColor: 'rgba(255, 255, 255, 0.23)',
  },
  '& .MuiSelect-select': {
    borderRadius: '4px',
  }
}));

interface SearchBarProps {
  onSearch: (query: string, contentType: string, recommendationCount: number) => void;
  isLoading: boolean;
}

const SearchBar = ({ onSearch, isLoading }: SearchBarProps) => {
  const [query, setQuery] = useState('');
  const [contentType, setContentType] = useState('movies');
  const [recommendationCount, setRecommendationCount] = useState(4);

  const handleSearch = () => {
    if (query.trim()) {
      onSearch(query.trim(), contentType, recommendationCount);
    }
  };

  const handleKeyPress = (event: KeyboardEvent<HTMLDivElement>) => {
    if (event.key === 'Enter') {
      handleSearch();
    }
  };

  const handleContentTypeChange = (
    event: SelectChangeEvent<unknown>
  ) => {
    const newContentType = event.target.value as string;
    setContentType(newContentType);
    
    if (query.trim()) {
      onSearch(query.trim(), newContentType, recommendationCount);
    }
  };

  return (
    <Box sx={{ 
      display: 'flex', 
      flexDirection: 'column', 
      gap: 3, 
      width: '100%', 
      mt: 10 
    }}>
      <Box sx={{ 
        display: 'flex', 
        gap: 3,
        alignItems: 'flex-start', 
        width: '100%',
      }}>
        <StyledFormControl>
          <InputLabel sx={{ 
            transform: 'translate(14px, -20px) scale(0.75)',
            left: '-6%',
            top: '-5%',
            '&.Mui-focused': { color: '#1976d2' }
          }}>
            Content Type
          </InputLabel>
          <StyledSelect
            value={contentType}
            label="Content Type"
            onChange={handleContentTypeChange}
            MenuProps={{
              PaperProps: {
                sx: {
                  backgroundColor: '#141414',
                  mt: 1,
                  '& .MuiList-root': {
                    padding: 0
                  }
                }
              },
              MenuListProps: {
                disablePadding: true,
                sx: {
                  padding: 0
                }
              },
              sx: {
                '& .MuiList-root': {
                  padding: 0,
                  '& .MuiMenuItem-root': {
                    margin: 0,
                    width: '100%',
                    display: 'block',
                    padding: '8px 16px',
                    '&:hover': {
                      backgroundColor: '#1976d2'
                    },
                  }
                }
              }
            }}
          >
            <MenuItem value="movies">Movies</MenuItem>
            <MenuItem value="shows">TV shows</MenuItem>
          </StyledSelect>
        </StyledFormControl>

        <StyledTextField
          fullWidth
          placeholder={`Enter ${contentType === 'movies' ? 'movie' : 'TV show'}`}
          value={query}
          onChange={(event) => setQuery(event.target.value)}
          onKeyPress={handleKeyPress}
          InputProps={{
            endAdornment: (
              <InputAdornment position="end">
                <IconButton 
                  onClick={handleSearch}
                  disabled={isLoading}
                  sx={{ color: 'white' }}
                >
                  {isLoading ? <CircularProgress size={24} color="inherit" /> : <SearchIcon />}
                </IconButton>
              </InputAdornment>
            ),
          }}
        />

        <StyledFormControl sx={{ flex: '0 0 auto' }}>
          <InputLabel 
            sx={{ 
              fontSize: '1rem',
              transform: 'translate(0px, -40px) scale(0.75)',
              left: '-6%',
              top: '-5%',
              '&.Mui-focused': { color: '#1976d2' }
            }}
          >
            Number of recommendations
          </InputLabel>
          <StyledSelect
            value={recommendationCount}
            onChange={(event) => setRecommendationCount(Number(event.target.value))}
            sx={{ 
              width: '200px',
              '& .MuiOutlinedInput-notchedOutline': {
                borderColor: 'rgba(255, 255, 255, 0.23)',
              }
            }}
          >
            <MenuItem value={2}>2 recommendations</MenuItem>
            <MenuItem value={3}>3 recommendations</MenuItem>
            <MenuItem value={4}>4 recommendations</MenuItem>
            <MenuItem value={5}>5 recommendations</MenuItem>
            <MenuItem value={10}>10 recommendations</MenuItem>
          </StyledSelect>
        </StyledFormControl>
      </Box>
    </Box>
  );
};

export default SearchBar;
