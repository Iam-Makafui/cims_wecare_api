-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 05, 2024 at 01:41 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `welfare_management_system_dev`
--

-- --------------------------------------------------------

--
-- Table structure for table `api_tokens`
--

CREATE TABLE `api_tokens` (
  `id` int(11) NOT NULL,
  `token` varchar(255) NOT NULL,
  `expiration_date` datetime NOT NULL,
  `inserted_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT NULL ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `api_tokens`
--

INSERT INTO `api_tokens` (`id`, `token`, `expiration_date`, `inserted_at`, `updated_at`) VALUES
(1, 'sdkoskdomoewokokso23o2k3230jiwejiweji32', '2025-01-01 12:00:00', '2023-12-19 20:45:43', '2023-12-19 21:03:08');

-- --------------------------------------------------------

--
-- Table structure for table `cases`
--

CREATE TABLE `cases` (
  `id` int(11) NOT NULL,
  `case_type_id` int(11) NOT NULL,
  `title` varchar(100) NOT NULL,
  `description` text NOT NULL,
  `beneficiary_id` int(11) NOT NULL,
  `case_status` varchar(50) NOT NULL,
  `issued_aid` float NOT NULL,
  `user_id` int(11) NOT NULL,
  `inserted_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT NULL ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `cases`
--

INSERT INTO `cases` (`id`, `case_type_id`, `title`, `description`, `beneficiary_id`, `case_status`, `issued_aid`, `user_id`, `inserted_at`, `updated_at`) VALUES
(1, 1, 'Funeral Contributions for ABC', 'This is a demo text, feel free to ignore it', 1, 'active', 10.05, 2, '2023-12-22 14:57:18', '2023-12-22 14:57:23'),
(2, 1, 'Test Case', 'ABCDEFGH.......XYZ', 1, 'closed', 0.01, 2, '2023-12-22 15:05:31', NULL),
(5, 1, 'Funeral Contributions for XYZ', 'This is a demo text, feel free to ignore it', 1, 'closed', 0, 2, '2023-12-27 12:41:09', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `case_contributions`
--

CREATE TABLE `case_contributions` (
  `id` bigint(20) NOT NULL,
  `case_id` int(11) NOT NULL,
  `member_id` int(11) NOT NULL,
  `amount` float NOT NULL,
  `user_id` int(11) NOT NULL,
  `inserted_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT NULL ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `case_contributions`
--

INSERT INTO `case_contributions` (`id`, `case_id`, `member_id`, `amount`, `user_id`, `inserted_at`, `updated_at`) VALUES
(1, 2, 1, 100, 2, '2023-12-27 12:49:58', '2023-12-27 12:52:33');

-- --------------------------------------------------------

--
-- Table structure for table `case_types`
--

CREATE TABLE `case_types` (
  `id` int(11) NOT NULL,
  `case_type` varchar(100) NOT NULL,
  `inserted_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT NULL ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `case_types`
--

INSERT INTO `case_types` (`id`, `case_type`, `inserted_at`, `updated_at`) VALUES
(1, 'Funeral Contribution', '2023-12-22 10:24:20', '2023-12-22 10:26:30');

-- --------------------------------------------------------

--
-- Table structure for table `dues`
--

CREATE TABLE `dues` (
  `id` bigint(20) NOT NULL,
  `member_id` int(11) NOT NULL,
  `amount` float NOT NULL,
  `approval_status` varchar(100) NOT NULL,
  `payment_method` varchar(100) NOT NULL,
  `month_and_year` varchar(100) NOT NULL,
  `user_id` int(11) NOT NULL,
  `inserted_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT NULL ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `dues`
--

INSERT INTO `dues` (`id`, `member_id`, `amount`, `approval_status`, `payment_method`, `month_and_year`, `user_id`, `inserted_at`, `updated_at`) VALUES
(1, 1, 10, 'pending', 'cash', '02-2023', 2, '2023-12-28 12:55:40', NULL),
(2, 2, 15, 'approved', 'momo', '01-2024', 2, '2023-12-28 12:56:40', '2023-12-28 13:00:39');

-- --------------------------------------------------------

--
-- Table structure for table `expenses`
--

CREATE TABLE `expenses` (
  `id` int(11) NOT NULL,
  `expense_type_id` int(11) NOT NULL,
  `description` text NOT NULL,
  `amount` float NOT NULL,
  `date` date DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  `inserted_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT NULL ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `expenses`
--

INSERT INTO `expenses` (`id`, `expense_type_id`, `description`, `amount`, `date`, `user_id`, `inserted_at`, `updated_at`) VALUES
(1, 1, 'Purchase was made for 100 cedis sms bundles', 100, '2024-01-05', 2, '2024-01-02 19:03:07', '2024-01-02 19:06:33');

-- --------------------------------------------------------

--
-- Table structure for table `expense_types`
--

CREATE TABLE `expense_types` (
  `id` int(11) NOT NULL,
  `expense_type` varchar(100) NOT NULL,
  `inserted_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT NULL ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `expense_types`
--

INSERT INTO `expense_types` (`id`, `expense_type`, `inserted_at`, `updated_at`) VALUES
(1, 'SMS Bundles', '2024-01-02 10:06:40', '2024-01-02 10:11:16');

-- --------------------------------------------------------

--
-- Table structure for table `members`
--

CREATE TABLE `members` (
  `id` int(11) NOT NULL,
  `member_id` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `inserted_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT NULL ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `members`
--

INSERT INTO `members` (`id`, `member_id`, `name`, `inserted_at`, `updated_at`) VALUES
(1, 'NL001', 'Micheal', '2023-12-21 13:07:12', '2023-12-21 13:07:15'),
(2, 'NLO02', 'David', '2023-12-27 12:45:32', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `roles`
--

CREATE TABLE `roles` (
  `id` int(11) NOT NULL,
  `role_name` varchar(255) NOT NULL,
  `inserted_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT NULL ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `roles`
--

INSERT INTO `roles` (`id`, `role_name`, `inserted_at`, `updated_at`) VALUES
(4, 'supervisor', '2023-12-19 21:04:26', NULL),
(5, 'admin', '2023-12-19 21:04:36', '2023-12-19 21:47:49'),
(6, 'user', '2023-12-19 22:09:28', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `firstname` varchar(100) DEFAULT NULL,
  `lastname` varchar(100) DEFAULT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `status` varchar(50) NOT NULL,
  `role_id` int(11) NOT NULL,
  `user_image` varchar(255) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT NULL ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `firstname`, `lastname`, `username`, `password`, `email`, `status`, `role_id`, `user_image`, `created_at`, `updated_at`) VALUES
(2, 'Kwame', 'Sefah', 'Kwams', 'ef797c8118f02dfb649607dd5d3f8c7623048c9c063d532cc95c5ed7a898a64f', 'test@hello.com', 'inactive', 6, '2930023.jpg', '2023-12-20 10:30:33', '2023-12-22 15:00:40'),
(5, NULL, NULL, 'Makafui', '0a2e5e03d616ebc2568aa7a71cc8ae1aff01c4ff56ba22bd5fba44c8ba4ca98b', 'test@makafui.com', 'active', 5, 'Makafui.png', '2023-12-20 14:06:34', NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `api_tokens`
--
ALTER TABLE `api_tokens`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `cases`
--
ALTER TABLE `cases`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fkcase_type` (`case_type_id`),
  ADD KEY `fkmember_case` (`beneficiary_id`),
  ADD KEY `fkusers_case` (`user_id`);

--
-- Indexes for table `case_contributions`
--
ALTER TABLE `case_contributions`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fkcase_contributions` (`case_id`),
  ADD KEY `fkmember_contributions` (`member_id`),
  ADD KEY `fkusers_contributions` (`user_id`);

--
-- Indexes for table `case_types`
--
ALTER TABLE `case_types`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `dues`
--
ALTER TABLE `dues`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fkmember_dues` (`member_id`),
  ADD KEY `fkusers_dues` (`user_id`);

--
-- Indexes for table `expenses`
--
ALTER TABLE `expenses`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fkexpense_type` (`expense_type_id`),
  ADD KEY `fkusers_expense` (`user_id`);

--
-- Indexes for table `expense_types`
--
ALTER TABLE `expense_types`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `members`
--
ALTER TABLE `members`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `roles`
--
ALTER TABLE `roles`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `email` (`email`),
  ADD KEY `fkuser_role` (`role_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `api_tokens`
--
ALTER TABLE `api_tokens`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `cases`
--
ALTER TABLE `cases`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `case_contributions`
--
ALTER TABLE `case_contributions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `case_types`
--
ALTER TABLE `case_types`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `dues`
--
ALTER TABLE `dues`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `expenses`
--
ALTER TABLE `expenses`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `expense_types`
--
ALTER TABLE `expense_types`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `members`
--
ALTER TABLE `members`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `roles`
--
ALTER TABLE `roles`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `cases`
--
ALTER TABLE `cases`
  ADD CONSTRAINT `fkcase_type` FOREIGN KEY (`case_type_id`) REFERENCES `case_types` (`id`),
  ADD CONSTRAINT `fkmember_case` FOREIGN KEY (`beneficiary_id`) REFERENCES `members` (`id`),
  ADD CONSTRAINT `fkusers_case` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

--
-- Constraints for table `case_contributions`
--
ALTER TABLE `case_contributions`
  ADD CONSTRAINT `fkcase_contributions` FOREIGN KEY (`case_id`) REFERENCES `cases` (`id`),
  ADD CONSTRAINT `fkmember_contributions` FOREIGN KEY (`member_id`) REFERENCES `members` (`id`),
  ADD CONSTRAINT `fkusers_contributions` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

--
-- Constraints for table `dues`
--
ALTER TABLE `dues`
  ADD CONSTRAINT `fkmember_dues` FOREIGN KEY (`member_id`) REFERENCES `members` (`id`),
  ADD CONSTRAINT `fkusers_dues` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

--
-- Constraints for table `expenses`
--
ALTER TABLE `expenses`
  ADD CONSTRAINT `fkexpense_type` FOREIGN KEY (`expense_type_id`) REFERENCES `expense_types` (`id`),
  ADD CONSTRAINT `fkusers_expense` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

--
-- Constraints for table `users`
--
ALTER TABLE `users`
  ADD CONSTRAINT `fkuser_role` FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
