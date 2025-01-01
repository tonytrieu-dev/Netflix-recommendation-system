import { Grid } from '@mui/material';
import MovieCard from '../MovieCard/MovieCard';
import { motion } from 'framer-motion';

interface RecommendationListProps {
  recommendations: string[];
}

const container = {
  hidden: { opacity: 0 },
  show: {
    opacity: 1,
    transition: {
      staggerChildren: 0.1
    }
  }
};

const RecommendationList = ({ recommendations }: RecommendationListProps) => {
  return (
    <motion.div
      variants={container}
      initial="hidden"
      animate="show"
    >
      <Grid container spacing={3}>
        {recommendations.map((title, index) => (
          <Grid item xs={12} sm={6} md={4} key={index}>
            <MovieCard title={title} />
          </Grid>
        ))}
      </Grid>
    </motion.div>
  );
};

export default RecommendationList;
