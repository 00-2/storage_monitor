--
-- PostgreSQL database dump
--

-- Dumped from database version 14.4 (Ubuntu 14.4-1.pgdg20.04+1)
-- Dumped by pg_dump version 14.4 (Ubuntu 14.4-1.pgdg20.04+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: storage_monitor; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE storage_monitor WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'en_US.UTF-8';


ALTER DATABASE storage_monitor OWNER TO postgres;

\connect storage_monitor

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: orders; Type: TABLE; Schema: public; Owner: test_user
--

CREATE TABLE IF NOT EXIST public.orders (
    order_table_id integer NOT NULL,
    order_num character varying(20) NOT NULL,
    cost_usd integer NOT NULL,
    cost_rub integer NOT NULL,
    delivery_date integer NOT NULL
);


ALTER TABLE public.orders OWNER TO test_user;

--
-- Name: orders_order_table_id_seq; Type: SEQUENCE; Schema: public; Owner: test_user
--

CREATE SEQUENCE public.orders_order_table_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.orders_order_table_id_seq OWNER TO test_user;

--
-- Name: orders_order_table_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: test_user
--

ALTER SEQUENCE public.orders_order_table_id_seq OWNED BY public.orders.order_table_id;


--
-- Name: orders order_table_id; Type: DEFAULT; Schema: public; Owner: test_user
--

ALTER TABLE ONLY public.orders ALTER COLUMN order_table_id SET DEFAULT nextval('public.orders_order_table_id_seq'::regclass);


--
-- Data for Name: orders; Type: TABLE DATA; Schema: public; Owner: test_user
--



--
-- Name: orders_order_table_id_seq; Type: SEQUENCE SET; Schema: public; Owner: test_user
--

SELECT pg_catalog.setval('public.orders_order_table_id_seq', 1, false);


--
-- Name: orders orders_pk; Type: CONSTRAINT; Schema: public; Owner: test_user
--

ALTER TABLE ONLY public.orders
    ADD CONSTRAINT orders_pk PRIMARY KEY (order_table_id);


--
-- Name: orders_order_num_uindex; Type: INDEX; Schema: public; Owner: test_user
--

CREATE UNIQUE INDEX orders_order_num_uindex ON public.orders USING btree (order_num);


--
-- Name: orders_order_table_id_uindex; Type: INDEX; Schema: public; Owner: test_user
--

CREATE UNIQUE INDEX orders_order_table_id_uindex ON public.orders USING btree (order_table_id);


--
-- Name: DATABASE storage_monitor; Type: ACL; Schema: -; Owner: postgres
--

GRANT ALL ON DATABASE storage_monitor TO test_user;


--
-- PostgreSQL database dump complete
--

