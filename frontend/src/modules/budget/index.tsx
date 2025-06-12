import React, {useState} from 'react';
export const BudgetView: React.FC = () => {
  const [filter,setFilter]=useState('high');
  return <div><h2>BUDGET - Budget - SF-424, budget, justification, </h2><p>SF-424</p></div>
};
export default BudgetView;
