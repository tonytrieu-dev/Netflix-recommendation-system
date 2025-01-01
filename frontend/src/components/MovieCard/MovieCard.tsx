import { Card, CardContent, Typography } from '@mui/material';
import { motion } from 'framer-motion';
import { styled } from '@mui/material/styles';

const StyledCard = styled(motion(Card))(({ theme }) => ({
  backgroundColor: '#181818',
  color: 'white',
  transition: 'all 0.3s ease',
  cursor: 'pointer',
  '&:hover': {
    transform: 'scale(1.05)',
    backgroundColor: '#282828',
  },
}));

interface MovieCardProps {
  title: string;
}

const MovieCard = ({ title }: MovieCardProps) => {
  return (
    <StyledCard
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.3 }}
    >
      <CardContent>
        <Typography variant="h6" component="div" sx={{ mb: 1 }}>
          {title}
        </Typography>
      </CardContent>
    </StyledCard>
  );
};

export default MovieCard;
