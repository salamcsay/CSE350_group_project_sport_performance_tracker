import { useState } from 'react';

/**
 * Custom hook for handling pagination
 * @param {number} initialPage - Initial page number (default: 1)
 * @param {number} initialPageSize - Initial page size (default: 10)
 * @returns {Object} Pagination utilities and handlers
 */
export const usePagination = (initialPage = 1, initialPageSize = 10) => {
  const [page, setPage] = useState(initialPage);
  const [pageSize, setPageSize] = useState(initialPageSize);

  const handlePageChange = (newPage) => {
    setPage(newPage);
  };

  const handlePageSizeChange = (newPageSize) => {
    setPageSize(newPageSize);
    setPage(1); // Reset to first page when changing page size
  };

  const getPaginatedData = (data = []) => {
    const start = (page - 1) * pageSize;
    const end = start + pageSize;
    return data.slice(start, end);
  };

  return {
    page,
    pageSize,
    handlePageChange,
    handlePageSizeChange,
    getPaginatedData,
    totalPages: (totalItems) => Math.ceil(totalItems / pageSize),
    isFirstPage: page === 1,
    isLastPage: (totalItems) => page === Math.ceil(totalItems / pageSize),
    startIndex: (totalItems) => Math.min((page - 1) * pageSize + 1, totalItems),
    endIndex: (totalItems) => Math.min(page * pageSize, totalItems)
  };
};