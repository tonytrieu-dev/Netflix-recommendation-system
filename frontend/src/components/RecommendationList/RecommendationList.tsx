import React from 'react';
import { Grid } from '@mui/material';
import { motion } from 'framer-motion';
import { ContentRecommendation } from '../../services/api';
import ContentCard from '../ContentCard/ContentCard';
import './RecommendationList.css';

interface RecommendationListProps {
  recommendations: ContentRecommendation[];
  contentType: string;
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

const RecommendationList = ({ recommendations, contentType }: RecommendationListProps) => {
  return (
    <motion.div
      variants={container}
      initial="hidden"
      animate="show"
      className="recommendation-container"
    >
      <Grid container spacing={3}>
        {recommendations.map((item) => (
          <Grid item xs={12} sm={6} md={4} lg={3} key={item.title}>
            <ContentCard content={item} contentType={contentType} />
          </Grid>
        ))}
      </Grid>
    </motion.div>
  );
};

export default RecommendationList;
