import logging

logging.basicConfig(level=logging.INFO)

file_path = "Day-2/Day2_input.txt"  # Path to the test input file

safe_cnt = 0

with open(file_path, "r") as f:
    for line in f:
        report = [int(x) for x in line.split()]  # Convert each line into a list of integers
        logging.info(report)
        if all(i < j for i, j in zip(report, report[1:])):
            if all(j - i <= 3 for i, j in zip(report, report[1:])):
                logging.info("Safely increasing")
                safe_cnt += 1
            else:
                logging.info("Dangerously increasing")
        elif all(i > j for i, j in zip(report, report[1:])):
            if all(j - i >= -3 for i, j in zip(report, report[1:])):
                logging.info("Safely decreasing")
                safe_cnt += 1
            else:
                logging.info("Dangerously decreasing")
        else:
            logging.info("Dangerously random")

logging.info("Safe reports: %s", safe_cnt)
