import { useState } from 'react';

/**
 * Custom hook for handling table sorting functionality
 * @param {string} initialSort - Initial column to sort by
 * @returns {Object} Sorting utilities and handlers
 */

export const useSortableTable = (initialSort = '') => {
  const [sortColumn, setSortColumn] = useState(initialSort);
  const [sortDirection, setSortDirection] = useState('asc');

  /**
   * Handle column header click for sorting
   * @param {string} column - Column identifier
   */

  const handleSort = (column) => {
    if (sortColumn === column) {
      setSortDirection(sortDirection === 'asc' ? 'desc' : 'asc');
    } else {
      setSortColumn(column);
      setSortDirection('asc');
    }
  };

  /**
   * Sort data array based on current sort settings
   * @param {Array} data - Array of data to sort
   * @param {Function} getValue - Optional function to get value from item
   * @returns {Array} Sorted array
   */

  const getSortedData = (data, getValue = (item, column) => item[column]) => {
    if (!sortColumn) return data;

    return [...data].sort((a, b) => {
      const aValue = getValue(a, sortColumn);
      const bValue = getValue(b, sortColumn);

      if (typeof aValue === 'string') {
        return sortDirection === 'asc'
          ? aValue.localeCompare(bValue)
          : bValue.localeCompare(aValue);
      }

      return sortDirection === 'asc'
        ? aValue - bValue
        : bValue - aValue;
    });
  };

  return {
    sortColumn,
    sortDirection,
    handleSort,
    getSortedData,
    isSortedAsc: sortDirection === 'asc',
    isSortedDesc: sortDirection === 'desc',
    getSortIcon: (column) => {
      if (sortColumn !== column) return '↕️';
      return sortDirection === 'asc' ? '↑' : '↓';
    }
  };
};