import { useState, KeyboardEvent } from 'react';
import { TextField, InputAdornment, IconButton } from '@mui/material';
import SearchIcon from '@mui/icons-material/Search';
import { styled } from '@mui/material/styles';

const StyledTextField = styled(TextField)(({ theme }) => ({
  '& .MuiInputBase-root': {
    color: 'white',
    backgroundColor: '#333',
    borderRadius: '4px',
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
      borderColor: '#e50914',
    },
  },
  '& .MuiInputBase-input': {
    padding: '12px 14px',
  },
}));

interface SearchBarProps {
  onSearch: (query: string) => void;
}

const SearchBar = ({ onSearch }: SearchBarProps) => {
  const [query, setQuery] = useState('');

  const handleSearch = () => {
    if (query.trim()) {
      onSearch(query.trim());
    }
  };

  const handleKeyPress = (event: KeyboardEvent<HTMLDivElement>) => {
    if (event.key === 'Enter') {
      handleSearch();
    }
  };

  return (
    <StyledTextField
      fullWidth
      placeholder="Enter a movie or TV show title..."
      value={query}
      onChange={(e) => setQuery(e.target.value)}
      onKeyPress={handleKeyPress}
      InputProps={{
        endAdornment: (
          <InputAdornment position="end">
            <IconButton onClick={handleSearch} sx={{ color: 'white' }}>
              <SearchIcon />
            </IconButton>
          </InputAdornment>
        ),
      }}
    />
  );
};

export default SearchBar;
